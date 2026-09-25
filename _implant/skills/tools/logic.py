#!/usr/bin/env python3
"""Propositional validity checker — implements the "logical" claim type of the
implant's conventions (conventions/how-claims-are-graded.md).

Usage:
  logic.py check <argument.json> [--json]
  logic.py check --premises "P -> Q" "P" --conclusion "Q" [--json]

JSON input: {"name": ..., "premises": [...], "conclusion": ..., "atoms": {...}}.
Syntax: atoms are identifiers; ~/not, &/and, |/or, ->, <-> and parentheses;
precedence ~ > & > | > -> > <->, with -> right-associative.
Method: full truth-table enumeration (at most 20 atoms). Reports validity,
counterexamples, inconsistent premises, tautological conclusions, redundant
premises, and names the classical schema the argument matches, if any.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from dataclasses import dataclass
from typing import Any, Union

MAX_ATOMS = 20
MAX_COUNTEREXAMPLES_SHOWN = 10


# --------------------------------------------------------------------------- AST

@dataclass(frozen=True)
class Atom:
    name: str


@dataclass(frozen=True)
class Not:
    operand: "Expr"


@dataclass(frozen=True)
class BinOp:
    op: str  # "&", "|", "->", "<->"
    left: "Expr"
    right: "Expr"


Expr = Union[Atom, Not, BinOp]


def to_str(e: Expr) -> str:
    if isinstance(e, Atom):
        return e.name
    if isinstance(e, Not):
        inner = to_str(e.operand)
        if isinstance(e.operand, BinOp):
            inner = f"({inner})"
        return f"~{inner}"
    return f"({to_str(e.left)} {e.op} {to_str(e.right)})"


def atoms_of(e: Expr, acc: set[str] | None = None) -> set[str]:
    if acc is None:
        acc = set()
    if isinstance(e, Atom):
        acc.add(e.name)
    elif isinstance(e, Not):
        atoms_of(e.operand, acc)
    else:
        atoms_of(e.left, acc)
        atoms_of(e.right, acc)
    return acc


def evaluate(e: Expr, env: dict[str, bool]) -> bool:
    if isinstance(e, Atom):
        return env[e.name]
    if isinstance(e, Not):
        return not evaluate(e.operand, env)
    a = evaluate(e.left, env)
    b = evaluate(e.right, env)
    if e.op == "&":
        return a and b
    if e.op == "|":
        return a or b
    if e.op == "->":
        return (not a) or b
    if e.op == "<->":
        return a == b
    raise ValueError(f"unknown operator {e.op!r}")


# ------------------------------------------------------------------------ Parser

class ParseError(ValueError):
    def __init__(self, message: str, position: int, text: str):
        self.position = position
        self.text = text
        super().__init__(f"{message} at position {position} in {text!r}")


@dataclass
class Token:
    kind: str  # "ATOM", "NOT", "AND", "OR", "IMP", "IFF", "LP", "RP", "EOF"
    text: str
    pos: int


_WORD_OPS = {"not": "NOT", "and": "AND", "or": "OR"}


def tokenize(text: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c.isspace():
            i += 1
            continue
        if text.startswith("<->", i):
            tokens.append(Token("IFF", "<->", i))
            i += 3
        elif text.startswith("->", i):
            tokens.append(Token("IMP", "->", i))
            i += 2
        elif c == "~":
            tokens.append(Token("NOT", c, i))
            i += 1
        elif c == "&":
            tokens.append(Token("AND", c, i))
            i += 1
        elif c == "|":
            tokens.append(Token("OR", c, i))
            i += 1
        elif c == "(":
            tokens.append(Token("LP", c, i))
            i += 1
        elif c == ")":
            tokens.append(Token("RP", c, i))
            i += 1
        elif c.isalpha() or c == "_":
            j = i
            while j < n and (text[j].isalnum() or text[j] == "_"):
                j += 1
            word = text[i:j]
            kind = _WORD_OPS.get(word.lower())
            if kind is not None and word.lower() == word:
                tokens.append(Token(kind, word, i))
            else:
                tokens.append(Token("ATOM", word, i))
            i = j
        else:
            raise ParseError(f"unexpected character {c!r}", i, text)
    tokens.append(Token("EOF", "", n))
    return tokens


class Parser:
    """Recursive descent: iff > imp (right-assoc) > or > and > not > primary."""

    def __init__(self, text: str):
        self.text = text
        self.tokens = tokenize(text)
        self.i = 0

    def peek(self) -> Token:
        return self.tokens[self.i]

    def advance(self) -> Token:
        t = self.tokens[self.i]
        self.i += 1
        return t

    def parse(self) -> Expr:
        e = self.parse_iff()
        t = self.peek()
        if t.kind != "EOF":
            raise ParseError(f"unexpected {t.text!r}", t.pos, self.text)
        return e

    def parse_iff(self) -> Expr:
        left = self.parse_imp()
        while self.peek().kind == "IFF":
            self.advance()
            right = self.parse_imp()
            left = BinOp("<->", left, right)
        return left

    def parse_imp(self) -> Expr:
        left = self.parse_or()
        if self.peek().kind == "IMP":
            self.advance()
            right = self.parse_imp()  # right-associative
            return BinOp("->", left, right)
        return left

    def parse_or(self) -> Expr:
        left = self.parse_and()
        while self.peek().kind == "OR":
            self.advance()
            left = BinOp("|", left, self.parse_and())
        return left

    def parse_and(self) -> Expr:
        left = self.parse_not()
        while self.peek().kind == "AND":
            self.advance()
            left = BinOp("&", left, self.parse_not())
        return left

    def parse_not(self) -> Expr:
        if self.peek().kind == "NOT":
            self.advance()
            return Not(self.parse_not())
        return self.parse_primary()

    def parse_primary(self) -> Expr:
        t = self.peek()
        if t.kind == "ATOM":
            self.advance()
            return Atom(t.text)
        if t.kind == "LP":
            self.advance()
            e = self.parse_iff()
            t2 = self.peek()
            if t2.kind != "RP":
                found = repr(t2.text) if t2.text else "end of input"
                raise ParseError(f"expected ')' but found {found}", t2.pos, self.text)
            self.advance()
            return e
        if t.kind == "EOF":
            raise ParseError("unexpected end of input, expected an atom or '('", t.pos, self.text)
        raise ParseError(f"unexpected {t.text!r}, expected an atom or '('", t.pos, self.text)


def parse(text: str) -> Expr:
    if not text.strip():
        raise ParseError("empty formula", 0, text)
    return Parser(text).parse()


# ----------------------------------------------------------------- Schema match

# Schemas use pattern variables A, B, C, D bound to arbitrary sub-formulas.
_SCHEMAS: list[tuple[str, list[str], str, bool]] = [
    ("modus ponens", ["A -> B", "A"], "B", True),
    ("modus tollens", ["A -> B", "~B"], "~A", True),
    ("hypothetical syllogism", ["A -> B", "B -> C"], "A -> C", True),
    ("disjunctive syllogism", ["A | B", "~A"], "B", True),
    ("constructive dilemma", ["A -> B", "C -> D", "A | C"], "B | D", True),
    ("affirming the consequent", ["A -> B", "B"], "A", False),
    ("denying the antecedent", ["A -> B", "~A"], "~B", False),
]


def _match(pattern: Expr, target: Expr, binding: dict[str, Expr]) -> bool:
    if isinstance(pattern, Atom):
        bound = binding.get(pattern.name)
        if bound is None:
            binding[pattern.name] = target
            return True
        return bound == target
    if isinstance(pattern, Not):
        return isinstance(target, Not) and _match(pattern.operand, target.operand, binding)
    return (
        isinstance(target, BinOp)
        and target.op == pattern.op
        and _match(pattern.left, target.left, binding)
        and _match(pattern.right, target.right, binding)
    )


def match_schema(premises: list[Expr], conclusion: Expr) -> str | None:
    """Return the schema name if the argument matches one exactly (premise
    order-insensitive, atoms/sub-formulas bound to pattern variables)."""
    for name, pat_prem, pat_concl, valid in _SCHEMAS:
        if len(pat_prem) != len(premises):
            continue
        pats = [parse(p) for p in pat_prem]
        pc = parse(pat_concl)
        for perm in itertools.permutations(premises):
            binding: dict[str, Expr] = {}
            if all(_match(p, t, binding) for p, t in zip(pats, perm)) and _match(
                pc, conclusion, binding
            ):
                return f"{name}{'' if valid else ' (invalid)'}"
    return None


# ----------------------------------------------------------------------- Check

def _is_valid(premises: list[Expr], conclusion: Expr, atoms: list[str]) -> bool:
    for values in itertools.product([True, False], repeat=len(atoms)):
        env = dict(zip(atoms, values))
        if all(evaluate(p, env) for p in premises) and not evaluate(conclusion, env):
            return False
    return True


def check(premise_texts: list[str], conclusion_text: str) -> dict[str, Any]:
    premises = [parse(p) for p in premise_texts]
    conclusion = parse(conclusion_text)
    atoms = sorted(set().union(*[atoms_of(p) for p in premises], atoms_of(conclusion)))
    if len(atoms) > MAX_ATOMS:
        raise ValueError(
            f"refusing: {len(atoms)} atoms exceeds the cap of {MAX_ATOMS} "
            f"(2^{len(atoms)} rows)"
        )

    counterexamples: list[dict[str, bool]] = []
    premises_satisfiable = False
    conclusion_tautology = True
    for values in itertools.product([True, False], repeat=len(atoms)):
        env = dict(zip(atoms, values))
        all_prem = all(evaluate(p, env) for p in premises)
        concl = evaluate(conclusion, env)
        if all_prem:
            premises_satisfiable = True
            if not concl:
                counterexamples.append(env)
        if not concl:
            conclusion_tautology = False

    valid = not counterexamples
    redundant: list[int] = []
    if valid and len(premises) > 1:
        for i in range(len(premises)):
            rest = premises[:i] + premises[i + 1:]
            if _is_valid(rest, conclusion, atoms):
                redundant.append(i + 1)

    return {
        "premises": premise_texts,
        "conclusion": conclusion_text,
        "parsed_premises": [to_str(p) for p in premises],
        "parsed_conclusion": to_str(conclusion),
        "atoms": atoms,
        "valid": valid,
        "counterexamples": counterexamples,
        "counterexample_count": len(counterexamples),
        "inconsistent_premises": bool(premises) and not premises_satisfiable,
        "tautological_conclusion": conclusion_tautology,
        "redundant_premises": redundant,
        "schema": match_schema(premises, conclusion),
    }


# ---------------------------------------------------------------------- Report

def format_report(result: dict[str, Any], name: str | None, atom_desc: dict[str, str]) -> str:
    lines: list[str] = []
    if name:
        lines.append(f"Argument: {name}")
    for i, (raw, parsed) in enumerate(zip(result["premises"], result["parsed_premises"]), 1):
        lines.append(f"  P{i}: {raw}    [{parsed}]")
    lines.append(f"  C:  {result['conclusion']}    [{result['parsed_conclusion']}]")
    if atom_desc:
        lines.append("Atoms:")
        for a in result["atoms"]:
            desc = atom_desc.get(a)
            lines.append(f"  {a}: {desc}" if desc else f"  {a}")
    lines.append("")
    lines.append("VALID" if result["valid"] else "INVALID")
    if not result["valid"]:
        shown = result["counterexamples"][:MAX_COUNTEREXAMPLES_SHOWN]
        lines.append("Counterexamples (premises true, conclusion false):")
        for env in shown:
            lines.append("  " + ", ".join(f"{a}={'T' if v else 'F'}" for a, v in env.items()))
        total = result["counterexample_count"]
        if total > len(shown):
            lines.append(f"  ... {total - len(shown)} more ({total} counterexample rows in total)")
        else:
            lines.append(f"  ({total} counterexample row{'s' if total != 1 else ''})")
    if result["inconsistent_premises"]:
        lines.append("premises are jointly inconsistent — argument is vacuously valid")
    if result["tautological_conclusion"]:
        lines.append("conclusion is a tautology — the argument is valid regardless of premises")
    for i in result["redundant_premises"]:
        lines.append(f"premise {i} is not needed for validity")
    if result["schema"]:
        lines.append(f"matches schema: {result['schema']}")
    return "\n".join(lines)


# ------------------------------------------------------------------------- CLI

def build_argparser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="logic.py",
        description="Propositional validity checker by truth-table enumeration.",
        epilog=(
            "Syntax: atoms are identifiers; operators ~/not, &/and, |/or, ->, <->; "
            "precedence ~ > & > | > -> > <->; -> is right-associative."
        ),
    )
    sub = ap.add_subparsers(dest="command", required=True)
    c = sub.add_parser("check", help="check an argument for validity")
    c.add_argument("file", nargs="?", help="JSON file with premises/conclusion")
    c.add_argument("--premises", nargs="+", metavar="FORMULA", help="premise formulas")
    c.add_argument("--conclusion", metavar="FORMULA", help="conclusion formula")
    c.add_argument("--json", action="store_true", help="machine-readable output")
    return ap


def main(argv: list[str] | None = None) -> int:
    ap = build_argparser()
    args = ap.parse_args(argv)

    name: str | None = None
    atom_desc: dict[str, str] = {}
    if args.file:
        if args.premises or args.conclusion:
            ap.error("give either a JSON file or --premises/--conclusion, not both")
        try:
            with open(args.file, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"error: cannot read {args.file}: {exc}", file=sys.stderr)
            return 2
        if not isinstance(data, dict) or "premises" not in data or "conclusion" not in data:
            print("error: JSON must be an object with 'premises' and 'conclusion'", file=sys.stderr)
            return 2
        premises = list(data["premises"])
        conclusion = str(data["conclusion"])
        name = data.get("name")
        atom_desc = dict(data.get("atoms") or {})
    else:
        if not args.premises or not args.conclusion:
            ap.error("need a JSON file, or both --premises and --conclusion")
        premises = args.premises
        conclusion = args.conclusion

    try:
        result = check(premises, conclusion)
    except ParseError as exc:
        print(f"parse error: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        out = dict(result)
        if name is not None:
            out["name"] = name
        print(json.dumps(out, indent=2))
    else:
        print(format_report(result, name, atom_desc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
