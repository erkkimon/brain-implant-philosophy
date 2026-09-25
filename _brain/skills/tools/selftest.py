#!/usr/bin/env python3
"""Self-test for logic.py and neutrality-lint.py (stdlib only, no pytest).

Usage: python3 selftest.py   — exits non-zero on any failure.
"""
from __future__ import annotations

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod  # dataclasses need the module registered before exec
    sys.dont_write_bytecode = True
    spec.loader.exec_module(mod)
    return mod


logic = load("logic", "logic.py")
lint = load("neutrality_lint", "neutrality-lint.py")

failures: list[str] = []
passed = 0


def check(cond: bool, label: str) -> None:
    global passed
    if cond:
        passed += 1
    else:
        failures.append(label)
        print(f"FAIL: {label}")


# ------------------------------------------------------------------ logic.py

r = logic.check(["P -> Q", "P"], "Q")
check(r["valid"], "modus ponens is valid")
check(r["schema"] == "modus ponens", f"modus ponens schema named (got {r['schema']!r})")
check(r["redundant_premises"] == [], "modus ponens has no redundant premise")

r = logic.check(["P -> Q", "Q"], "P")
check(not r["valid"], "affirming the consequent is invalid")
check(r["counterexamples"] == [{"P": False, "Q": True}], "exactly one counterexample P=F,Q=T")
check(r["schema"] == "affirming the consequent (invalid)", "affirming the consequent named")

r = logic.check(["P", "~P"], "Q")
check(r["valid"] and r["inconsistent_premises"], "inconsistent premises detected")

r = logic.check(["P -> Q", "P", "R"], "Q")
check(r["valid"] and r["redundant_premises"] == [3], "redundant premise 3 detected")

try:
    logic.parse("P ->")
    check(False, "parse error for 'P ->'")
except logic.ParseError as exc:
    check(exc.position == 4, f"parse error position is 4 (got {exc.position})")

e = logic.parse("P <-> Q")
table = [(p, q, logic.evaluate(e, {"P": p, "Q": q})) for p in (True, False) for q in (True, False)]
check(table == [(True, True, True), (True, False, False), (False, True, False), (False, False, True)],
      "biconditional truth table")

e = logic.parse("P -> Q -> R")
check(e == logic.BinOp("->", logic.Atom("P"), logic.BinOp("->", logic.Atom("Q"), logic.Atom("R"))),
      "-> is right-associative")
check(logic.parse("not P and Q or R") == logic.parse("(~P & Q) | R"), "word operators and precedence")
check(logic.check(["P -> Q", "~Q"], "~P")["schema"] == "modus tollens", "modus tollens named")
check(logic.check(["A | B", "~A"], "B")["schema"] == "disjunctive syllogism", "disjunctive syllogism named")
r = logic.check(["P"], "Q | ~Q")
check(r["valid"] and r["tautological_conclusion"], "tautological conclusion detected")

# ---------------------------------------------------------- neutrality-lint.py

f, s = lint.lint_text("This is a fallacy.\n")
check(len(f) == 1 and f[0]["label"] == "fallacy", "bare 'fallacy' is flagged")

f, _ = lint.lint_text("Walton classifies this as a fallacy (Walton 2008, p. 19).\n")
check(f == [], "attributed + cited sentence is not flagged")

f, _ = lint.lint_text("It is a fallacy (Walton 2008).\n")
check(f == [], "citation-only sentence is not flagged")

f, _ = lint.lint_text("> This is obviously a fallacy.\n")
check(f == [], "blockquote is not flagged")

f, _ = lint.lint_text('He wrote "this is obviously a fallacy" and left.\n')
check(f == [], "double-quoted string is not flagged")

f, _ = lint.lint_text("He wrote “this is obviously a fallacy” and left.\n")
check(f == [], "curly-quoted string is not flagged")

f, s = lint.lint_text("This is obviously a fallacy. # lint: allow\n")
check(f == [] and s == 2, f"'# lint: allow' suppresses (suppressed={s})")

f, _ = lint.lint_text("---\ntitle: The fallacy\n---\n\nText. See `fallacy` here.\n\n```\nobviously\n```\n")
check(f == [], "frontmatter, inline code, fenced code are not flagged")

f, _ = lint.lint_text("# Critique\n\nSome say so. This is naive.\n")
check(len(f) == 1 and f[0]["section"] == "Critique" and f[0]["attribution_section"],
      "heading context and attribution-section flag reported")

f, _ = lint.lint_text("Smith argues it fails. It clearly does.\n")
check(len(f) == 1 and f[0]["word"] == "clearly", "attribution does not leak across sentences")

f, _ = lint.lint_text("It is in fact true.\n")
check(len(f) == 1 and f[0]["severity"] == "weak", "'in fact' is flagged as weak")

# --------------------------------------------------------------------- result

if failures:
    print(f"{len(failures)} failure(s), {passed} passed")
    sys.exit(1)
print(f"selftest OK: {passed} checks passed (logic.py, neutrality-lint.py)")
