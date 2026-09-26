# Analytic proof — the T2 off-chart sign factor (U-B7-2)

**Date:** 2026-09-26
**Target:** the Book 7 companion-cosine identity row `7.1.T2` in
`book7_claims.md`; the NOTATION_LEDGER row U-B7-2 (vol4, "ε (T2, off-chart)",
previously ASSERTED).
**Verdict: PROVED** — exact algebra. Conditional on Lemma 7.2 (PROVED) and the
identity statement itself. Each algebraic identity below was verified by two
independent machine routes: local sympy and a WolframAlpha browser session
(2026-09-26, 6 queries, 6 answered; session file
`../wa_sessions/2026-09-26-1051.md`). Per standing label discipline the WA
results are recorded as independent corroboration of the hand algebra, not as
the proof.

## Theorem

In `cos2x = ε(1−2λ)√(1+4λ(1−λ))` with `λ = (1+sin x−cos x)/2`, the sign factor
must be **ε = sgn(cos x + sin x)** wherever `1+sin2x > 0`. The sign factor
written in the claim files, `ε = sgn(sin x)·sgn(cos x)`, is wrong on the
intervals `(π/2, 3π/4)`, `(π, 3π/2)`, `(7π/4, 2π)` (mod 2π), where it makes the
identity false.

## Proof

**S1 — substitution.** By Lemma 7.2 (PROVED): `1−2λ = cos x−sin x` and
`4λ(1−λ) = sin2x`. Hence the identity's right-hand side is exactly
`RHS = ε(cos x−sin x)√(1+sin2x)`.

**S2 — square identity (minus).** `(cos x−sin x)² = 1−sin2x`.
Machine check: `Simplify[(Cos[x]-Sin[x])^2-(1-Sin[2*x])] = 0` (WA Q1, sympy).

**S3 — square identity (plus).** `(cos x+sin x)² = 1+sin2x`.
Machine check: `Simplify[(Cos[x]+Sin[x])^2-(1+Sin[2*x])] = 0` (WA Q2, sympy).

**S4 — squared identity.** Using S1–S2:
`RHS² = (cos x−sin x)²(1+sin2x) = (1−sin2x)(1+sin2x) = 1−sin²2x = cos²2x = LHS²`.
Machine check: `Simplify[(1-Sin[2*x])*(1+Sin[2*x])-Cos[2*x]^2] = 0`
(WA Q3, sympy). So `|RHS| = |LHS|` for every x.

**S5 — factor the left side.** `cos2x = (cos x−sin x)(cos x+sin x)`.
Machine check: `Simplify[Cos[2*x]-(Cos[x]-Sin[x])*(Cos[x]+Sin[x])] = 0`
(WA Q4, sympy).

**S6 — the sign is forced.** `√(1+sin2x) ≥ 0` always. On
`U = {x : 1+sin2x > 0, cos x−sin x ≠ 0}`: `sgn(RHS) = ε·sgn(cos x−sin x)`
(the radical is strictly positive), while by S5
`sgn(LHS) = sgn(cos x−sin x)·sgn(cos x+sin x)`, where `sgn(cos x+sin x)` is
well-defined and nonzero because `(cos x+sin x)² = 1+sin2x > 0` on U (S3).
Cancelling `sgn(cos x−sin x) ≠ 0` gives `ε = sgn(cos x+sin x)` on all of U.

**S7 — the complement (both sides vanish).**
(a) `1+sin2x = 0 ⇔ x = 3π/4 + kπ`: `LHS = cos(3π/2+2kπ) = 0`;
`RHS = ε(cos x−sin x)·0 = 0`. Holds for any ε.
(b) `cos x−sin x = 0 ⇔ x = π/4 + kπ`: `LHS = cos(π/2+kπ) = 0`;
`RHS = ε·0·√(1+sin2x) = 0`. Holds for any ε.
So ε is forced exactly where both sides are nonzero, and is undetermined but
irrelevant where both vanish.

**S8 — the manuscript ε is wrong where it disagrees.**
`sgn(sin x)·sgn(cos x) = sgn(sin2x)`. The two candidates differ exactly where
`sin2x` and `cos x+sin x` have opposite signs. Machine check:
`Reduce[Sin[2*x]*(Cos[x]+Sin[x])<0 && 0<=x<2*Pi, x, Reals]` returns
`π/2 < x < 3π/4 ∨ π < x < 3π/2 ∨ 7π/4 < x < 2π` (WA Q5, sympy independently).
There the manuscript ε assigns the wrong sign and the identity fails — e.g.
at `x = 2.0`: `sgn(sin 4.0) = −1` but `sgn(cos 2.0+sin 2.0) = +1` (WA Q6,
sympy), matching the 2026-09-22 session's residual `−1.30729` under the
manuscript ε and `0` under the corrected ε.

**Sufficiency.** With `ε = sgn(cos x+sin x)`: on U, S6 gives matching signs
and S4 gives matching magnitudes, so `RHS = LHS`; off U both sides vanish
(S7). The identity holds for all real x. ∎

## Scope and what this closes

- Promotes U-B7-2 from ASSERTED to PROVED (exact algebra, conditional on
  Lemma 7.2 PROVED; WA + sympy independent machine corroboration).
- Fills the §INCOMPLETE gap in `book7_claims.md`: the off-chart analytic
  branch proof for 7.1.T2 now exists; row 7.1.T2 is PROVED on all charts.
- The two ε's coincide on `(3π/4, π)` and `(3π/2, 7π/4)` — consistent with the
  2026-09-22 session's Q2/Q4 (both residuals 0 there).
- Does not touch the transfer-domain ε = sgn(sin2x) used in 7.4 (a different
  object, the saw-transfer ε); that usage is unaffected.
