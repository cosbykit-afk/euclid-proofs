# Campaign seed theorem: Kit's double-angle secant/cosecant identity

Scope: PROVED (analytic, complete). Source: ~/workspace/kit_theorems/secant-cosecant-identity/PROOF.md
Attribution: Kit Cosby, shared 2026-09-21. Verified by agent 2026-09-22: the proof in
the source file is complete and accurate (positivity argument, both lemmas, regrouping,
and the domain-redundancy argument all checked correct). Its numerical check
(500,000 samples, worst |LHS − RHS| = 7.8e−07, pure float rounding) is consistent
with but not needed by the analytic proof.

This theorem is established. Every book's proof in this campaign may cite it
without re-proving it.

## Statement

For all real x with sin(x) ≠ 0 and cos(x) ≠ 0
(the condition sin(2x) ≠ 0 is redundant — it is equivalent to the conjunction):

    4/sin(2x) = (tan(x) + |sec(x)| − 1/(cot(x) + |csc(x)|))
              + (cot(x) + |csc(x)| − 1/(tan(x) + |sec(x)|))

## Proof (definitions first)

Definitions: for real x with cos(x) ≠ 0 and sin(x) ≠ 0,
tan(x) = sin(x)/cos(x), sec(x) = 1/cos(x), cot(x) = cos(x)/sin(x), csc(x) = 1/sin(x),
and |·| is the ordinary real absolute value.

Set A = tan(x) + |sec(x)| and B = cot(x) + |csc(x)|.

Positivity: |sec(x)| − |tan(x)| = (1 − |sin(x)|)/|cos(x)| > 0, because
cos(x) ≠ 0 implies |sin(x)| < 1. Hence A ≥ |sec(x)| − |tan(x)| > 0.
Likewise B ≥ |csc(x)| − |cot(x)| = (1 − |cos(x)|)/|sin(x)| > 0.
So A, B are strictly positive, and 1/A, 1/B are defined.

Lemma 1: A − 1/A = 2·tan(x).
A² = tan²(x) + 2·tan(x)·|sec(x)| + |sec(x)|². Since |sec(x)|² = sec²(x) = 1 + tan²(x),
  A² − 1 = 2·tan²(x) + 2·tan(x)·|sec(x)| = 2·tan(x)·A.
Divide by A > 0: A − 1/A = 2·tan(x). ∎

Lemma 2: B − 1/B = 2·cot(x). Same argument with cot/csc. ∎

Regroup the right-hand side (addition commutes):
  (A − 1/B) + (B − 1/A) = (A − 1/A) + (B − 1/B)
                        = 2·tan(x) + 2·cot(x)      (Lemmas 1, 2)
                        = 2·(sin(x)/cos(x) + cos(x)/sin(x))
                        = 2/(sin(x)·cos(x))
                        = 4/sin(2x). ∎

Domain remark: sin(2x) = 2·sin(x)·cos(x), so sin(2x) ≠ 0 ⟺ sin(x) ≠ 0 ∧ cos(x) ≠ 0.
No separate condition is needed. No quadrant case split is needed either: the
absolute values are absorbed by |sec(x)|² = sec²(x).

Status: PROVED.
