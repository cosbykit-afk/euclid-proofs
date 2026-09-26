# Book 10 ledger — proposition inventory, proof dependencies, R Theory extension mapping

**Source text:** `/home/hatch/workspace/euclid_work/text/book10.txt` (Fitzpatrick/Heiberg translation, 7,720 lines).
**Generated:** 2026-09-22. **Method:** machine extraction of enunciations and bracketed proof citations, verified proposition-by-proposition against the source (see §9).

## 1. Historical frame (from the encyclopedia article)

- Book X is the classification of irrationals. The material is attributed to **Theaetetus** (cf. Plato, *Theaetetus* 147D) and **Eudoxus**; Pappus wrote a commentary on it (Arabic text with Thomson/Junge translation).
- The first irrational isolated is the **medial**: the side of a square equal in area to a rectangle whose sides are commensurable in square only.
- Euclid then defines **six pairs of compound irrationals** (each pair differing in sign only) — the positive roots of six biquadratics reducible to quadratics, of the form x⁴ ± 2alx² ± bl⁴ = 0. The first pair are the **binomial** and the **apotome**; the other four are the two bimedials, the major, and the square-roots of (rational + medial) and (two medials).
- From these he derives **six further pairs**, the roots of six quadratics of the form x² + 2alx + bl² = 0.
- In all, **some twenty-five irrational line-forms** are investigated across the **115 propositions** — *of which the last four (112–115) may be interpolations* (encyclopedia article).
- The book's purpose is downstream: the irrational lines classified here are the ones that occur in the constructions of the regular solids in Book XIII.

**TESS framing note.** The TESS-India OER paper (*Developing creative thinking in mathematics: trigonometry*) contributes no proof or dependency to this ledger. It is used only as pedagogical framing: linking concepts of shape and space with ratio, deduction, and mathematical proof through creative, experimental thinking — the same creative-deductive register in which Book X's classifications were originally produced.

## 2. Definitions (16, in three groups)

| No. | Definition |
|---|---|
| 10.Def.1 | Magnitudes measured by the same measure are **commensurable**; those admitting no common measure are **incommensurable**. |
| 10.Def.2 | Straight-lines are **commensurable in square** when the squares on them are measured by the same area; otherwise **incommensurable in square**. |
| 10.Def.3 | Infinitely many lines exist commensurable and incommensurable (in length and in square) with an assigned line; the assigned line is called **rational**, and lines commensurable with it (in length or in square only) are rational. |
| 10.Def.4 | The square on the assigned line is called **rational**; areas commensurable with it are **rational**, incommensurable ones **irrational**, and their square-roots irrational. |
| 10.Def.5 | Given a rational and a divided binomial, if the square on the greater exceeds the square on the lesser by the square on a line length-commensurable with the greater, and the greater is length-commensurable with the laid-out rational: **first binomial**. |
| 10.Def.6 | Same, but the *lesser* term length-commensurable with the rational: **second binomial**. |
| 10.Def.7 | Same, but *neither* term length-commensurable with the rational: **third binomial**. |
| 10.Def.8 | Square-excess by a line length-*incommensurable* with the greater, greater term length-commensurable with the rational: **fourth binomial**. |
| 10.Def.9 | Same, lesser term length-commensurable: **fifth binomial**. |
| 10.Def.10 | Same, neither term length-commensurable: **sixth binomial**. |
| 10.Def.11 | Given a rational and an apotome: if the square on the whole exceeds the square on the attached line by the square on a line length-commensurable with the whole, and the whole is length-commensurable with the rational: **first apotome**. |
| 10.Def.12 | Same, but the *attached* line length-commensurable with the rational (excess commensurable): **second apotome**. |
| 10.Def.13 | Same, *neither* length-commensurable with the rational (excess commensurable): **third apotome**. |
| 10.Def.14 | Square-excess by a line length-*incommensurable* with the whole, whole length-commensurable with the rational: **fourth apotome**. |
| 10.Def.15 | Same, attached line length-commensurable: **fifth apotome**. |
| 10.Def.16 | Same, neither length-commensurable: **sixth apotome**. |

Full extracted wording is preserved in `/tmp/book10_parsed.json` under `definitions`.

## 3. Postulates and common notions

**Book 10 introduces no new postulates and no new common notions.** All constructions use Book 1 postulates; all inferences use the existing common notions and the definitions above. This is stated explicitly rather than omitted: the dependency lists below contain no Book-10 postulate or common-notion entries because none exist in the source.

## 4. Dependency-notation key

- `Prop. N.M` — Euclid, Book N, Proposition M (Fitzpatrick/Heiberg numbering).
- `Def. 10.K` — Book 10 definition K.
- `(corr.)` — the cited item is a **corollary** of the proposition.
- `(lem.)`, `(lem. I)`, `(lem. II)` — the cited item is a **lemma** attached to the proposition (lemmas I/II of 10.28; the lemma of 10.13, 10.21, 10.32, 10.38, 10.41, 10.53, 10.59).
- Citations are the translator's bracketed proof references as printed; they were machine-extracted and are listed in printed order with duplicates removed.

## 5. Propositions 10.1–10.115

Extension column: every row reads ∅ — no R Theory book or claim that builds on or generalizes the proposition was located (exhaustive full-text search of rewrite books 0–22; see §7). Scope column therefore carries no PROVED/CHECKED/ASSERTED/INCOMPLETE label: there is no extension claim to scope.

| Prop. | One-line statement | Proof dependencies (as printed) | R Theory extension | Scope |
|---|---|---|---|---|
| 10.1 | Repeatedly subtracting more than half eventually leaves less than the lesser of two unequal magnitudes (exhaustion principle). | Def. 5.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.2 | If the anthyphairetic remainder process never terminates, the two magnitudes are incommensurable. | Def. 10.1 | ∅ — no R Theory claim located (see §7) | — |
| 10.3 | Construct the greatest common measure of two commensurable magnitudes. | Prop. 10.2 | ∅ — no R Theory claim located (see §7) | — |
| 10.4 | Construct the greatest common measure of three commensurable magnitudes. | Prop. 10.3; Prop. 10.3 (corr.); Def. 10.1 | ∅ — no R Theory claim located (see §7) | — |
| 10.5 | Commensurable magnitudes are in the ratio of some number to some number. | Def. 7.20; Prop. 5.7 (corr.); Prop. 5.22 | ∅ — no R Theory claim located (see §7) | — |
| 10.6 | Magnitudes in the ratio of number to number are commensurable. | Def. 7.20; Prop. 5.7 (corr.); Prop. 5.22; Prop. 5.11; Prop. 5.9; Def. 10.1; Prop. 6.19 (corr.) | ∅ — no R Theory claim located (see §7) | — |
| 10.7 | Incommensurable magnitudes are not in the ratio of number to number. | Prop. 10.6 | ∅ — no R Theory claim located (see §7) | — |
| 10.8 | Magnitudes not in the ratio of number to number are incommensurable. | Prop. 10.5 | ∅ — no R Theory claim located (see §7) | — |
| 10.9 | Commensurability in length holds iff the squares are in the ratio of a square number to a square number. | Prop. 10.5; Prop. 6.20 (corr.); Prop. 8.11; Prop. 10.6 | ∅ — no R Theory claim located (see §7) | — |
| 10.10 | Construct two lines incommensurable with a given line: one in length only, one in square as well. (Heiberg: interpolation.) | Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 6.13; Def. 5.9; Prop. 10.11 | ∅ — no R Theory claim located (see §7) | — |
| 10.11 | Proportionality preserves commensurability (resp. incommensurability) across the two pairs. | Prop. 10.5; Prop. 10.6; Prop. 10.7; Prop. 10.8 | ∅ — no R Theory claim located (see §7) | — |
| 10.12 | Magnitudes commensurable with the same magnitude are commensurable with one another. | Prop. 10.5; Prop. 8.4; Prop. 5.11; Prop. 5.22; Prop. 10.6 | ∅ — no R Theory claim located (see §7) | — |
| 10.13 | Incommensurability with an outside magnitude transfers across two commensurable magnitudes. | Prop. 10.12; Prop. 4.1; Prop. 3.31; Prop. 1.47 | ∅ — no R Theory claim located (see §7) | — |
| 10.14 | In a proportion of lines, 'square-excess by a commensurable (resp. incommensurable) line' transfers across the pairs. | Prop. 6.22; Prop. 5.17; Prop. 5.7 (corr.); Prop. 5.22; Prop. 10.11 | ∅ — no R Theory claim located (see §7) | — |
| 10.15 | Sum or difference of commensurables is commensurable with each of them. | Def. 10.1 | ∅ — no R Theory claim located (see §7) | — |
| 10.16 | Sum or difference involving an incommensurable is incommensurable with each term. | Def. 10.1 | ∅ — no R Theory claim located (see §7) | — |
| 10.17 | Quarter-square application: commensurable division iff square-excess by a line commensurable with the greater. | Prop. 1.10; Prop. 1.3; Prop. 2.5; Prop. 10.15; Prop. 10.6; Prop. 10.12 | ∅ — no R Theory claim located (see §7) | — |
| 10.18 | Quarter-square application: incommensurable division iff square-excess by a line incommensurable with the greater. | Prop. 10.16; Prop. 10.6; Prop. 10.13 | ∅ — no R Theory claim located (see §7) | — |
| 10.19 | The rectangle of length-commensurable rational lines is rational. | Def. 10.4; Prop. 6.1; Prop. 10.11 | ∅ — no R Theory claim located (see §7) | — |
| 10.20 | A rational area on a rational side gives a rational breadth, length-commensurable with the side. | Def. 10.4; Prop. 6.1; Prop. 10.11; Def. 10.3 | ∅ — no R Theory claim located (see §7) | — |
| 10.21 | The rectangle of square-only-commensurable rational lines is irrational; its side is irrational — the medial. | Def. 10.4; Prop. 6.1; Prop. 10.11 | ∅ — no R Theory claim located (see §7) | — |
| 10.22 | A medial square on a rational side gives a rational breadth incommensurable in length with the side. | Prop. 10.21; Prop. 6.14; Prop. 6.22; Prop. 10.11; Def. 10.4; Prop. 10.13 | ∅ — no R Theory claim located (see §7) | — |
| 10.23 | A line commensurable with a medial line is medial. | Prop. 10.22; Prop. 6.1; Prop. 10.11; Def. 10.3; Prop. 10.13; Prop. 10.21 | ∅ — no R Theory claim located (see §7) | — |
| 10.24 | The rectangle of length-commensurable medial lines is medial. | Prop. 6.1; Prop. 10.11; Prop. 10.23 (corr.) | ∅ — no R Theory claim located (see §7) | — |
| 10.25 | The rectangle of square-only-commensurable medial lines is rational or medial. | Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.19; Prop. 5.11; Prop. 6.17; Prop. 10.21 | ∅ — no R Theory claim located (see §7) | — |
| 10.26 | A medial area cannot exceed a medial area by a rational area. | Prop. 10.22; Prop. 10.20; Prop. 10.13; Prop. 10.13 (lem.); Prop. 10.11; Prop. 10.6; Prop. 2.4; Prop. 10.16; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.27 | Construct two square-only-commensurable medials containing a rational area. | Prop. 6.13; Prop. 6.12; Prop. 6.17; Prop. 10.21; Prop. 10.11; Prop. 10.23; Prop. 5.16; Prop. 5.11 | ∅ — no R Theory claim located (see §7) | — |
| 10.28 | Construct two square-only-commensurable medials containing a medial area. | Prop. 6.13; Prop. 6.12; Prop. 6.17; Prop. 10.21; Prop. 10.11; Prop. 10.23; Prop. 5.16; Prop. 6.16; Prop. 9.24; Prop. 9.26; Prop. 2.6; Prop. 9.1 | ∅ — no R Theory claim located (see §7) | — |
| 10.29 | Construct two square-only-commensurable rationals whose square-excess is by a length-commensurable line. | Prop. 10.28 (lem. I); Prop. 10.6 (corr.); Prop. 10.6; Def. 10.4; Prop. 10.9; Prop. 5.19 (corr.), Prop. 3.31, Prop. 1.47; Prop. 1.47 | ∅ — no R Theory claim located (see §7) | — |
| 10.30 | Construct two square-only-commensurable rationals whose square-excess is by a length-incommensurable line. | Prop. 10.28 (lem. II); Prop. 10.6 (corr); Prop. 5.19 (corr.), Prop. 3.31, Prop. 1.47; Prop. 10.9; Prop. 1.47 | ∅ — no R Theory claim located (see §7) | — |
| 10.31 | Construct two square-only-commensurable medials containing a rational area, square-excess by a length-commensurable line. | Prop. 10.29; Prop. 10.21; Prop. 10.21 (lem.); Prop. 10.11; Prop. 10.23; Prop. 10.14; Prop. 10.30 | ∅ — no R Theory claim located (see §7) | — |
| 10.32 | Construct two square-only-commensurable medials containing a medial area, square-excess by a length-commensurable line. | Prop. 10.29; Prop. 10.21; Prop. 10.21 (lem.); Prop. 10.11; Prop. 10.23; Prop. 10.14; Prop. 10.30; Prop. 6.8; Prop. 6.4; Prop. 6.17; Prop. 6.8 (corr.); Prop. 6.16 | ∅ — no R Theory claim located (see §7) | — |
| 10.33 | Construct two square-incommensurable lines with rational sum of squares and medial contained rectangle. | Prop. 10.30; Prop. 6.28; Prop. 10.18; Prop. 10.32 (lem.); Prop. 10.11; Prop. 1.47; Prop. 10.6; Prop. 10.21; Prop. 10.23 (corr.) | ∅ — no R Theory claim located (see §7) | — |
| 10.34 | Construct two square-incommensurable lines with medial sum of squares and rational contained rectangle. | Prop. 10.31; Prop. 6.28; Prop. 10.18; Prop. 10.11; Prop. 10.32 (lem.); Prop. 3.31; Prop. 1.47; Prop. 10.6, Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.35 | Construct two square-incommensurable lines with medial sum of squares and medial contained rectangle incommensurable with that sum. | Prop. 10.32; Prop. 10.18; Prop. 10.11; Prop. 3.31; Prop. 1.47; Prop. 10.32 (lem.); Prop. 10.13 | ∅ — no R Theory claim located (see §7) | — |
| 10.36 | The sum of two square-only-commensurable rationals is irrational — the binomial. | Prop. 10.11; Prop. 10.6; Prop. 10.15; Prop. 10.13; Prop. 2.4; Prop. 10.16; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.37 | The sum of two square-only-commensurable medials containing a rational area is irrational — the first bimedial. | Prop. 2.4; Prop. 10.16; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.38 | The sum of two square-only-commensurable medials containing a medial area is irrational — the second bimedial. | Prop. 10.28; Prop. 1.44; Prop. 2.4; Prop. 10.22; Prop. 10.21 (lem.); Prop. 10.11; Prop. 10.15; Prop. 10.6; Prop. 10.13; Prop. 6.1; Prop. 10.36; Prop. 10.20; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.39 | The sum of two square-incommensurable lines (rational sum of squares, medial rectangle) is irrational — the major. | Prop. 10.33; Prop. 10.6 (corr.); Prop. 10.23 (corr.); Def. 10.4; Prop. 2.4; Prop. 10.16 | ∅ — no R Theory claim located (see §7) | — |
| 10.40 | The sum of two square-incommensurable lines (medial sum of squares, rational rectangle) is irrational — the square-root of a rational plus a medial. | Prop. 10.34; Prop. 10.16; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.41 | The sum of two square-incommensurable lines (medial sum of squares, medial rectangle incommensurable with it) is irrational — the square-root of two medials. | Prop. 10.35; Prop. 2.4; Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.36; Def. 10.4; Prop. 2.5 | ∅ — no R Theory claim located (see §7) | — |
| 10.42 | A binomial divides into its component terms at one point only. | Prop. 10.36; Prop. 2.4; Prop. 10.21; Prop. 10.26 | ∅ — no R Theory claim located (see §7) | — |
| 10.43 | A first bimedial divides into its component terms at one point only. | Prop. 10.37; Prop. 10.41 (lem.); Prop. 10.26 | ∅ — no R Theory claim located (see §7) | — |
| 10.44 | A second bimedial divides into its component terms at one point only. | Prop. 10.38; Prop. 10.41 (lem.); Prop. 2.4; Prop. 10.22; Prop. 10.21 (lem.); Prop. 10.11; Prop. 10.15; Prop. 10.6; Prop. 10.13; Prop. 6.1; Prop. 10.36; Prop. 10.42; Prop. 10.59 (lem.) | ∅ — no R Theory claim located (see §7) | — |
| 10.45 | A major divides into its component terms at one point only. | Prop. 10.39; Prop. 10.26 | ∅ — no R Theory claim located (see §7) | — |
| 10.46 | A square-root of a rational plus a medial divides into its component terms at one point only. | Prop. 10.40; Prop. 10.26 | ∅ — no R Theory claim located (see §7) | — |
| 10.47 | A square-root of two medials divides into its component terms at one point only. | Prop. 10.41; Prop. 2.4; Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.36; Prop. 10.42 | ∅ — no R Theory claim located (see §7) | — |
| 10.48 | Construct a first binomial. | Prop. 10.28 (lem. I); Def. 10.3; Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.36; Prop. 5.14; Prop. 5.19 (corr.); Prop. 10.9; Def. 10.5 | ∅ — no R Theory claim located (see §7) | — |
| 10.49 | Construct a second binomial. | Prop. 10.28 (lem. I); Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.36; Prop. 5.7 (corr.); Prop. 5.14; Prop. 5.19 (corr.); Def. 10.6 | ∅ — no R Theory claim located (see §7) | — |
| 10.50 | Construct a third binomial. | Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.36; Prop. 5.22; Prop. 5.14; Prop. 5.19 (corr.); Def. 10.7 | ∅ — no R Theory claim located (see §7) | — |
| 10.51 | Construct a fourth binomial. | Prop. 10.28 (lem. I); Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.36; Prop. 5.14; Prop. 5.19 (corr.); Def. 10.8 | ∅ — no R Theory claim located (see §7) | — |
| 10.52 | Construct a fifth binomial. | Prop. 10.38 (lem.); Prop. 10.6 (corr.); Prop. 10.9; Prop. 10.36; Prop. 5.7 (corr.); Prop. 5.14; Prop. 5.19 (corr.) | ∅ — no R Theory claim located (see §7) | — |
| 10.53 | Construct a sixth binomial. | Prop. 10.28 (lem. I); Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.36; Prop. 5.22; Prop. 5.14; Prop. 5.19 (corr.); Def. 10.10; Prop. 1.34; Prop. 6.1; Prop. 5.11; Prop. 5.18 | ∅ — no R Theory claim located (see §7) | — |
| 10.54 | Rational times first binomial: the square-root of the area is binomial. | Def. 10.5; Prop. 2.14; Prop. 10.53 (lem.); Prop. 6.17; Prop. 6.1; Prop. 1.43; Prop. 10.15; Prop. 10.12; Prop. 10.19; Prop. 10.13; Prop. 10.11; Prop. 10.36 | ∅ — no R Theory claim located (see §7) | — |
| 10.55 | Rational times second binomial: the square-root of the area is first bimedial. | Def. 10.6; Prop. 10.17; Prop. 10.53 (lem.); Prop. 10.13; Prop. 10.15; Prop. 10.21; Prop. 6.1; Prop. 10.11; Prop. 10.12; Prop. 10.19; Prop. 10.37 | ∅ — no R Theory claim located (see §7) | — |
| 10.56 | Rational times third binomial: the square-root of the area is second bimedial. | Def. 10.7; Prop. 10.13; Prop. 10.21; Prop. 10.38 | ∅ — no R Theory claim located (see §7) | — |
| 10.57 | Rational times fourth binomial: the square-root of the area is major. | Def. 10.8; Prop. 10.18; Prop. 6.1; Prop. 10.11; Prop. 10.19; Prop. 10.13; Prop. 10.21; Prop. 10.39 | ∅ — no R Theory claim located (see §7) | — |
| 10.58 | Rational times fifth binomial: the square-root of the area is the square-root of a rational plus a medial. | Prop. 10.18; Prop. 6.1; Prop. 10.11; Def. 10.9; Prop. 10.13; Prop. 10.21; Prop. 10.12; Prop. 10.19; Prop. 10.40 | ∅ — no R Theory claim located (see §7) | — |
| 10.59 | Rational times sixth binomial: the square-root of the area is the square-root of two medials. | Def. 10.10; Prop. 10.21; Prop. 10.13; Prop. 6.1; Prop. 10.11; Prop. 10.41; Prop. 2.5; Prop. 2.9 | ∅ — no R Theory claim located (see §7) | — |
| 10.60 | The square on a binomial, applied to a rational, gives a first binomial breadth. | Prop. 2.4; Prop. 10.36; Prop. 10.15; Prop. 10.20; Prop. 10.21; Prop. 10.22; Prop. 10.13; Prop. 10.53 (lem.); Prop. 6.1; Prop. 6.17; Prop. 10.11; Prop. 10.59 (lem.); Prop. 5.14; Prop. 10.17; Def. 10.5 | ∅ — no R Theory claim located (see §7) | — |
| 10.61 | The square on a first bimedial, applied to a rational, gives a second binomial breadth. | Prop. 10.37; Prop. 10.21; Prop. 10.15 (corr.); Prop. 10.23 (corr.); Prop. 10.22; Prop. 10.20; Prop. 10.13; Prop. 10.36; Prop. 10.59; Prop. 6.1; Prop. 10.11; Prop. 10.17 | ∅ — no R Theory claim located (see §7) | — |
| 10.62 | The square on a second bimedial, applied to a rational, gives a third binomial breadth. | Prop. 10.38; Prop. 10.15 (corr.); Prop. 10.23 (corr.); Prop. 10.22; Prop. 10.21 (lem.); Prop. 10.11; Prop. 10.12; Prop. 10.13; Prop. 6.1; Prop. 10.36; Prop. 10.17; Def. 10.7 | ∅ — no R Theory claim located (see §7) | — |
| 10.63 | The square on a major, applied to a rational, gives a fourth binomial breadth. | Prop. 10.39; Prop. 10.20; Prop. 10.22; Prop. 10.13; Prop. 10.36; Prop. 6.1; Prop. 10.11; Prop. 10.18; Def. 10.8 | ∅ — no R Theory claim located (see §7) | — |
| 10.64 | The square on a square-root of a rational plus a medial, applied to a rational, gives a fifth binomial breadth. | Prop. 10.40; Prop. 10.22; Prop. 10.20; Prop. 10.13; Prop. 10.36; Prop. 10.18; Def. 10.9 | ∅ — no R Theory claim located (see §7) | — |
| 10.65 | The square on a square-root of two medials, applied to a rational, gives a sixth binomial breadth. | Prop. 10.41; Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.36; Prop. 10.18; Def. 10.10 | ∅ — no R Theory claim located (see §7) | — |
| 10.66 | A line length-commensurable with a binomial is binomial of the same order. | Prop. 10.36; Prop. 6.12; Prop. 6.16 (corr.); Prop. 5.19 (corr.); Prop. 10.11; Prop. 5.11; Prop. 5.16; Prop. 10.14; Prop. 10.12; Def. 10.5; Def. 10.6; Prop. 10.13; Def. 10.7; Def. 10.8; Def. 10.9; Def. 10.10 | ∅ — no R Theory claim located (see §7) | — |
| 10.67 | A line length-commensurable with a bimedial is bimedial of the same order. | Prop. 10.37; Prop. 10.38; Prop. 6.12; Prop. 5.19 (corr.), Prop. 6.16; Prop. 10.11; Prop. 10.23; Prop. 10.21 (lem.); Prop. 5.16 | ∅ — no R Theory claim located (see §7) | — |
| 10.68 | A line length-commensurable with a major is major. | Prop. 10.39; Prop. 5.11; Prop. 10.11; Prop. 5.16; Prop. 5.18; Prop. 6.20; Prop. 10.23 (corr.) | ∅ — no R Theory claim located (see §7) | — |
| 10.69 | A line length-commensurable with a square-root of a rational plus a medial is the same. | Prop. 10.40 | ∅ — no R Theory claim located (see §7) | — |
| 10.70 | A line length-commensurable with a square-root of two medials is the same. | Prop. 10.41 | ∅ — no R Theory claim located (see §7) | — |
| 10.71 | Rational plus medial area: its square-root is a binomial, first bimedial, major, or square-root of a rational plus a medial. | Prop. 10.20; Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.36; Prop. 5.14; Def. 10.5; Prop. 10.54; Def. 10.8; Prop. 10.57; Def. 10.6; Prop. 10.55; Def. 10.9; Prop. 10.58 | ∅ — no R Theory claim located (see §7) | — |
| 10.72 | Sum of two incommensurable medial areas: its square-root is a second bimedial or a square-root of two medials. | Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.36; Def. 10.7; Prop. 10.56; Def. 10.10; Prop. 10.59; Prop. 10.60; Prop. 10.61; Prop. 10.62; Prop. 10.63; Prop. 10.64; Prop. 10.65 | ∅ — no R Theory claim located (see §7) | — |
| 10.73 | A rational minus a square-only-commensurable rational: the remainder is irrational — the apotome. | Prop. 10.21 (lem.); Prop. 10.11; Prop. 10.15; Prop. 10.6; Prop. 2.7; Prop. 10.13; Prop. 10.16; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.74 | A medial minus a square-only-commensurable medial containing a rational area with it: the remainder is irrational — first apotome of a medial. | Prop. 10.27; Prop. 2.7; Prop. 10.16; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.75 | A medial minus a square-only-commensurable medial containing a medial area with it: the remainder is irrational — second apotome of a medial. | Prop. 10.28; Prop. 2.7; Prop. 10.15 (corr.); Prop. 10.23 (corr.); Prop. 10.22; Prop. 10.21 (lem.), Prop. 10.11; Prop. 10.15; Prop. 10.6; Prop. 10.13; Prop. 6.1; Prop. 10.11; Prop. 10.73; Prop. 10.20; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.76 | A line minus a square-incommensurable line (rational sum of squares, medial rectangle): the remainder is irrational — the minor. | Prop. 10.33; Prop. 2.7; Prop. 10.16; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.77 | A line minus a square-incommensurable line (medial sum of squares, rational double rectangle): the remainder is irrational — that which with a rational area makes a medial whole. | Prop. 10.34; Prop. 2.7; Prop. 10.16; Def. 10.4 | ∅ — no R Theory claim located (see §7) | — |
| 10.78 | A line minus a square-incommensurable line (medial sum of squares, medial double rectangle incommensurable with it): the remainder is irrational — that which with a medial area makes a medial whole. | Prop. 10.35; Prop. 2.7; Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.73; Prop. 10.20 | ∅ — no R Theory claim located (see §7) | — |
| 10.79 | Only one square-only-commensurable rational line can be attached to an apotome. | Prop. 10.73; Prop. 2.7; Prop. 10.21; Prop. 10.26 | ∅ — no R Theory claim located (see §7) | — |
| 10.80 | Only one square-only-commensurable medial line containing a rational area with the whole can be attached to a first apotome of a medial. | Prop. 10.74; Prop. 2.7; Prop. 10.15 (corr.); Prop. 10.23 (corr.); Prop. 10.26 | ∅ — no R Theory claim located (see §7) | — |
| 10.81 | Only one square-only-commensurable medial line containing a medial area with the whole can be attached to a second apotome of a medial. | Prop. 10.75; Prop. 2.7; Prop. 10.15 (corr.); Prop. 10.23 (corr.); Prop. 10.22; Prop. 10.21 (corr.); Prop. 10.11; Prop. 10.6; Prop. 10.13; Prop. 6.1; Prop. 10.73; Prop. 10.79 | ∅ — no R Theory claim located (see §7) | — |
| 10.82 | Only one square-incommensurable line (rational sum of squares, medial double rectangle) can be attached to a minor. | Prop. 10.76; Prop. 2.7; Prop. 10.26 | ∅ — no R Theory claim located (see §7) | — |
| 10.83 | Only one square-incommensurable line (medial sum of squares, rational double rectangle) can be attached to a rational-plus-medial whole. | Prop. 10.77; Prop. 10.26 | ∅ — no R Theory claim located (see §7) | — |
| 10.84 | Only one square-incommensurable line (medial sum of squares, medial double rectangle incommensurable with it) can be attached to a medial-plus-medial whole. | Prop. 10.78; Prop. 2.7; Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.73; Prop. 10.79 | ∅ — no R Theory claim located (see §7) | — |
| 10.85 | Construct a first apotome. | Prop. 10.28 (lem. I); Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.73; Prop. 10.13 (lem.); Prop. 5.19 (corr.); Def. 10.11 | ∅ — no R Theory claim located (see §7) | — |
| 10.86 | Construct a second apotome. | Prop. 10.28 (lem. I); Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.73; Prop. 10.13 (lem.); Prop. 5.19 (corr.); Def. 10.12 | ∅ — no R Theory claim located (see §7) | — |
| 10.87 | Construct a third apotome. | Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.73; Prop. 5.22; Prop. 10.13 (lem.); Prop. 5.19 (corr.); Def. 10.13 | ∅ — no R Theory claim located (see §7) | — |
| 10.88 | Construct a fourth apotome. | Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.73; Prop. 10.13 (lem.); Prop. 5.19 (corr.); Def. 10.14 | ∅ — no R Theory claim located (see §7) | — |
| 10.89 | Construct a fifth apotome. | Prop. 10.6; Prop. 10.9; Prop. 10.73; Prop. 10.13 (lem.); Prop. 5.19 (corr.); Def. 10.15 | ∅ — no R Theory claim located (see §7) | — |
| 10.90 | Construct a sixth apotome. | Prop. 10.6 (corr.); Prop. 10.6; Prop. 10.9; Prop. 10.73; Prop. 5.22; Prop. 10.13 (lem.); Prop. 5.19 (corr.); Def. 10.16 | ∅ — no R Theory claim located (see §7) | — |
| 10.91 | Rational times first apotome: the square-root of the area is an apotome. | Prop. 10.73; Def. 10.11; Prop. 10.17; Prop. 10.15; Prop. 10.12; Prop. 10.19; Prop. 10.13; Prop. 10.21; Prop. 6.26; Prop. 6.17; Prop. 6.1; Prop. 5.11; Prop. 10.53 (lem.); Prop. 1.43; Prop. 10.11 | ∅ — no R Theory claim located (see §7) | — |
| 10.92 | Rational times second apotome: the square-root of the area is a first apotome of a medial. | Prop. 10.73; Def. 10.12; Prop. 10.17; Prop. 10.15; Prop. 10.13; Prop. 10.21; Prop. 10.19; Prop. 6.26; Prop. 6.1; Prop. 5.11; Prop. 10.53 (lem.); Prop. 1.43; Prop. 10.11; Prop. 10.74 | ∅ — no R Theory claim located (see §7) | — |
| 10.93 | Rational times third apotome: the square-root of the area is a second apotome of a medial. | Prop. 10.73; Def. 10.13; Prop. 10.17; Prop. 6.1; Prop. 10.11; Prop. 10.15; Prop. 10.13; Prop. 10.21; Prop. 6.26; Prop. 6.17; Prop. 5.11; Prop. 10.53 (lem.); Prop. 1.43; Prop. 10.75 | ∅ — no R Theory claim located (see §7) | — |
| 10.94 | Rational times fourth apotome: the square-root of the area is a minor. | Prop. 10.73; Def. 10.14; Prop. 10.18; Prop. 10.19; Prop. 10.21; Prop. 6.1; Prop. 10.11; Prop. 6.26; Prop. 6.17; Prop. 5.11; Prop. 10.13 (lem.); Prop. 1.43; Prop. 10.76 | ∅ — no R Theory claim located (see §7) | — |
| 10.95 | Rational times fifth apotome: the square-root of the area is a rational-plus-medial whole. | Prop. 10.73; Def. 10.15; Prop. 10.18; Prop. 10.21; Prop. 10.19; Prop. 6.26; Prop. 10.77 | ∅ — no R Theory claim located (see §7) | — |
| 10.96 | Rational times sixth apotome: the square-root of the area is a medial-plus-medial whole. | Prop. 10.73; Def. 10.16; Prop. 10.18; Prop. 6.1; Prop. 10.11; Prop. 10.21; Prop. 6.26; Prop. 10.78 | ∅ — no R Theory claim located (see §7) | — |
| 10.97 | The square on an apotome, applied to a rational, gives a first apotome breadth. | Prop. 10.73; Prop. 2.7; Prop. 10.20; Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.21 (lem.); Prop. 6.17; Prop. 10.17; Def. 10.15 | ∅ — no R Theory claim located (see §7) | — |
| 10.98 | The square on a first apotome of a medial, applied to a rational, gives a second apotome breadth. | Prop. 10.74; Prop. 10.15 (corr.); Prop. 10.23 (corr.); Prop. 10.22; Prop. 2.7; Prop. 10.20; Prop. 6.1; Prop. 10.11; Prop. 10.73; Prop. 10.21 (lem.); Prop. 5.11; Prop. 6.17; Prop. 10.17; Def. 10.16 | ∅ — no R Theory claim located (see §7) | — |
| 10.99 | The square on a second apotome of a medial, applied to a rational, gives a third apotome breadth. | Prop. 10.75; Prop. 10.15 (corr.); Prop. 10.23 (corr.); Prop. 10.22; Prop. 2.7; Prop. 6.1; Prop. 10.11; Prop. 10.13; Prop. 10.73; Prop. 10.21 (lem.); Prop. 5.11; Prop. 6.17; Prop. 10.17; Def. 10.13 | ∅ — no R Theory claim located (see §7) | — |
| 10.100 | The square on a minor, applied to a rational, gives a fourth apotome breadth. | Prop. 10.76; Prop. 10.20; Prop. 2.7; Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.73; Prop. 10.21 (lem.); Prop. 5.11; Prop. 6.17; Prop. 10.18; Def. 10.14 | ∅ — no R Theory claim located (see §7) | — |
| 10.101 | The square on a rational-plus-medial whole, applied to a rational, gives a fifth apotome breadth. | Prop. 10.77; Prop. 10.22; Prop. 2.7; Prop. 10.20; Prop. 6.1; Prop. 10.11; Prop. 10.73; Prop. 10.18; Def. 10.15 | ∅ — no R Theory claim located (see §7) | — |
| 10.102 | The square on a medial-plus-medial whole, applied to a rational, gives a sixth apotome breadth. | Prop. 10.78; Prop. 10.22; Prop. 2.7; Prop. 6.1; Prop. 10.11; Prop. 10.73; Prop. 10.21 (lem.); Prop. 10.18; Def. 10.16 | ∅ — no R Theory claim located (see §7) | — |
| 10.103 | A line length-commensurable with an apotome is an apotome of the same order. | Prop. 10.73; Prop. 6.12; Prop. 5.12; Prop. 10.11; Prop. 10.13; Prop. 5.16; Prop. 10.14; Prop. 10.12; Def. 10.11–10.16 | ∅ — no R Theory claim located (see §7) | — |
| 10.104 | A line length-commensurable with an apotome of a medial is the same, of the same order. | Prop. 10.74; Prop. 10.75; Prop. 6.12; Prop. 5.12; Prop. 10.11; Prop. 10.23; Prop. 10.13; Prop. 5.16; Prop. 10.21 (lem.); Def. 10.4; Prop. 10.23 (corr.) | ∅ — no R Theory claim located (see §7) | — |
| 10.105 | A line length-commensurable with a minor is a minor. | Prop. 10.76; Prop. 10.13; Prop. 5.12; Prop. 5.16; Prop. 6.22; Prop. 5.18; Prop. 10.104; Prop. 10.11; Def. 10.4; Prop. 10.21 (lem.); Prop. 10.23 (corr.) | ∅ — no R Theory claim located (see §7) | — |
| 10.106 | A line length-commensurable with a rational-plus-medial whole is the same. | Prop. 10.77 | ∅ — no R Theory claim located (see §7) | — |
| 10.107 | A line length-commensurable with a medial-plus-medial whole is the same. | Prop. 10.78 | ∅ — no R Theory claim located (see §7) | — |
| 10.108 | Rational minus medial area: its square-root is an apotome or a minor. | Prop. 10.20; Prop. 10.22; Prop. 10.13; Prop. 10.73; Def. 10.1; Prop. 10.91; Prop. 10.14; Prop. 10.94 | ∅ — no R Theory claim located (see §7) | — |
| 10.109 | Medial minus rational area: its square-root is a first apotome of a medial or a rational-plus-medial whole. | Prop. 10.13; Prop. 10.73; Def. 10.12; Prop. 10.92; Def. 10.15; Prop. 10.95 | ∅ — no R Theory claim located (see §7) | — |
| 10.110 | Medial minus an incommensurable medial area: its square-root is a second apotome of a medial or a medial-plus-medial whole. | Prop. 10.22; Prop. 6.1; Prop. 10.11; Prop. 10.73; Def. 10.3; Prop. 10.93; Def. 10.16; Prop. 10.96 | ∅ — no R Theory claim located (see §7) | — |
| 10.111 | An apotome is not the same as a binomial (the irrational classes are pairwise distinct). | Prop. 10.97; Def. 10.10; Prop. 10.60; Def. 10.5; Prop. 10.12; Prop. 10.15; Prop. 10.13; Prop. 10.73; Prop. 10.22; Prop. 10.98; Prop. 10.99; Prop. 10.100; Prop. 10.101; Prop. 10.102; Prop. 10.111 | ∅ — no R Theory claim located (see §7) | — |
| 10.112 | The square on a rational, applied to a binomial, gives an apotome breadth of the same order, its terms commensurable with the binomial's. | Prop. 6.16; Prop. 5.16; Prop. 5.14; Prop. 5.17; Prop. 5.12; Prop. 5.11; Prop. 10.36; Prop. 6.22; Prop. 10.11; Def. 5.9; Prop. 10.15; Prop. 10.20; Def. 10.3; Prop. 10.12; Prop. 10.73; Prop. 10.14; Def. 10.5–10.10 | ∅ — no R Theory claim located (see §7) | — |
| 10.113 | The square on a rational, applied to an apotome, gives a binomial breadth of the same order, its terms commensurable with the apotome's. | Prop. 10.73; Prop. 10.20; Prop. 6.16; Prop. 5.16; Prop. 5.14; Prop. 5.19 (corr.); Prop. 5.19; Prop. 10.11; Prop. 5.11; Def. 5.9; Prop. 10.15; Prop. 10.12; Def. 10.3, Prop. 10.13; Prop. 10.36; Prop. 10.14; Prop. 10.13; Def. 10.5–10.10 | ∅ — no R Theory claim located (see §7) | — |
| 10.114 | Apotome times order-matched binomial (terms commensurable, same ratio): the square-root of the area is rational. | Prop. 10.112; Prop. 5.16; Prop. 5.19; Prop. 10.12; Prop. 10.11; Prop. 6.1 | ∅ — no R Theory claim located (see §7) | — |
| 10.115 | Infinitely many distinct irrationals arise from a medial; none coincides with any preceding one. | Def. 10.4; Prop. 10.20 | ∅ — no R Theory claim located (see §7) | — |

## 6. Structure of the book (reading guide to the table)

- **10.1–10.18** — commensurability theory: the exhaustion principle (1), the anthyphairetic criterion (2), greatest common measures (3–4), number-ratio equivalences (5–9), existence of incommensurables (10), proportion transfer theorems (11–14), sums and differences (15–16), and the quarter-square application criteria (17–18).
- **10.19–10.26** — rational and medial: the medial defined and its arithmetic (19–26).
- **10.27–10.35** — constructions of the six generating pairs (27–35).
- **10.36–10.41** — the six additive irrationals proved irrational: binomial, two bimedials, major, √(rational+medial), √(two medials).
- **10.42–10.47** — uniqueness of division into terms for each of the six.
- **10.48–10.53** — construction of the six binomial orders.
- **10.54–10.65** — the binomial/apotome conversion ladder (54–59 areas; 60–65 squares applied to rationals).
- **10.66–10.72** — commensurability preserves class and order (66–70); the addition classification (71–72).
- **10.73–10.78** — the six subtractive irrationals proved irrational: apotome, two apotomes of a medial, minor, √(rational)+medial whole, √(medial)+medial whole.
- **10.79–10.84** — uniqueness of the attached line for each subtractive class.
- **10.85–10.90** — construction of the six apotome orders.
- **10.91–10.102** — the apotome conversion ladder, mirroring 54–65.
- **10.103–10.107** — commensurability preserves subtractive class and order.
- **10.108–10.110** — the subtraction classification, mirroring 71–72.
- **10.111** — apotome ≠ binomial; the classes are pairwise distinct.
- **10.112–10.114** — the binomial/apotome duality: rational square on a binomial gives an order-matched apotome and conversely; matched product has rational square-root.
- **10.115** — infinitely many distinct irrationals from a medial.

## 7. R Theory extension mapping — verdict

**No proposition of Book 10 is built on or generalized by any R Theory claim.** This is a verified negative result, not an omission:

- Full-text search of all 23 rewrite pages (`book0/`–`book22/`) for `incommensurab*`, `commensurab*`, `apotome`, `bimedial`, `medial`, `theaetetus`, `eudoxus`, `elements` (as Euclid's work), `hypsicles`, `pappus`: **zero relevant hits**. (The only `elements` hits are 'group elements', 'matrix elements', 'grade-four elements' — false positives.)
- The one Euclid mention in the series (Book 4, §4.X) is the **Euclidean postulate audit** with the **No-Euclid-wholesale theorem (4.X.H)** — an explicit refusal to import Euclid wholesale — and the **no-novelty-from-coordinate-change rule (4.X.I = Gate H)**. It concerns the postulates, not Book 10's irrational-line taxonomy.
- The audit ledgers concur: `DEPENDENCY_CHAIN.md` has no Euclid entries; `NOTATION_LEDGER.md` records only the imported premises below.
- R Theory's one visible brush with Book-10-adjacent values — exact constants such as √2 ± 1 (Book 1 phase charts) and √3/2 (Book 4 Flower coordinates, X = u + v/2, Y = (√3/2)v) — is **usage of real arithmetic, not an extension of Euclid 10.9/10.10 or of the binomial classification**. No source states such a dependency; none is claimed here.

Consequence: R Theory does not *extend* Book 10 — it *bypasses* it, taking the real continuum as declared substrate (see §8). The proposition table above therefore carries no extension entries and no scope labels; inventing them would violate the standing rule.

## 8. New load-bearing axioms/definitions beyond Euclid (exact list)

These are the R Theory primitives that occupy the foundational role where a Euclid-extension would otherwise have to construct the irrationals. Each is quoted from its source with the source's own status.

| # | Item | Content | Source | Status |
|---|---|---|---|---|
| 1 | **Axiom Zero A0.1** | Independent partner U♯ + declared block-compatible pairing ι + direct sum W = U ⊕ U♯ | Book 5, §5.2 | **AXIOM — granted, not proved** (NOTATION_LEDGER §0.5: 'First R-specific mathematical axiom in the revised chain') |
| 2 | **Axiom Zero A0.2** | Primitive diagonal noncoupling (off-diagonal maps in Hom(U,U♯) are mathematical, not active primitive couplings) | Book 5, §5.2 | **AXIOM — granted, not proved** |
| 3 | **P4.1** | Substrate (pre-metric synthetic substrate) — imported premise | Book 4 prep constitution; §§4.IV, 4.X | **AA (explicitly admitted)** |
| 4 | **P4.1-C** | SSS congruence — imported premise | Book 4 prep constitution; §§4.IV, 4.X | **AA (explicitly admitted)** |
| 5 | **P4.3** | Global Euclidean declaration (global flatness and unique parallels need this *separate* declaration) | Book 4 §4.X | **AA (explicitly admitted)** |
| 6 | **S1–S6** | Solid postulates (noncoplanar extension, …) | Book 4 §4.V | **AA (explicitly admitted)** |
| 7 | **Gates A–H** | Ordering gates (rank before dimension, …; Gate H = no-novelty-from-coordinate-change firewall) | Book 4 prep constitution | **Declared** |
| 8 | **4.X.H** | 'No-Euclid-wholesale theorem': Euclid is *not* imported wholesale | Book 4 §4.X | **Manuscript assertion** |
| 9 | **Real carriers E, V, U, W** | E = real rank-2 carrier, V = real rank-3 carrier, U = E ⊕ V (dim_ℝ 5), W = U ⊕ U♯ (dim_ℝ 10, the decadic carrier) | Book 5 §§5.1–5.3 | **Definitions** (dim counts exact: V1, V2) |

What is *not* on this list: any construction of √2, of incommensurable magnitudes, or of the binomial/apotome taxonomy from Euclid's definitions. R Theory assumes ℝ-linear structure at the substrate level (P4.1) rather than deriving irrationals à la Book 10. Nothing in the series re-proves, generalizes, or depends on a specific Book 10 proposition — see §7.

## 9. Method, verification, and disclosed limitations

**Extraction.** A parser (`/tmp/parse_book10.py`, output `/tmp/book10_parsed.json`) split the source on literal newlines (Python `splitlines()` was found to split on form-feed characters and shift source locations — corrected), isolated the English column of the two-column layout by cutting after the last Greek character per line, and collected bracketed citations `[Prop. …]`, `[Def. …]` from the proof bodies.

**Verified mechanically:**
- All 16 definitions present (10.Def.1–16), in the three definition groups; all 115 propositions present (10.1–10.115), no gaps, no duplicates.
- Proposition headers found at source lines 65 (Prop. 1) through 7685 (Prop. 115).

**Footnote exclusion (translator's apparatus, not Euclid's proofs).** The edition's †/‡/§/¶/∗/$ footnotes contain modern algebraic paraphrases with forward cross-references (e.g. `[Prop. 10.85]`–`[Prop. 10.90]` inside footnotes to Props. 48–53). A footnote region begins at a marker-start line and extends across blank lines, page headers, and math-continuation lines until the next Proposition/Lemma/Corollary header or fresh prose. Five such footnotes span page breaks; all five were verified to begin with the marker paragraph '† If the rational straight-line has unit length…'. These translator cross-references are excluded from the dependency lists above.

**Genuine forward citations retained:** Prop. 10.10 cites Prop. 10.11 in its proof (the edition's own footnote marks Prop. 10 as a Heiberg-suspected interpolation); Prop. 10.44 cites the lemma of Prop. 10.59.

**Limitations — stated plainly:**
- Dependency lists reproduce the *translator's printed citations*; they were not independently re-derived from the Greek, and no proposition was re-proved here. A missing citation in the print would be missing above.
- One-line statements are faithful condensations of the extracted enunciations; artifacts of the two-column layout (stray punctuation, truncated line-wraps) were cleaned by hand against the source.
- Prop. 10.111's proof closes with a self-citation `[Prop. 10.111]` — a recap ('it has been shown that an apotome is not the same as a binomial'), not a circular dependency; retained as printed.
- The encyclopedia article notes Props. 112–115 'may be interpolations'; this is reported as a manuscript-historical claim, not verified here.
- The R Theory negative result (§7) rests on full-text search of the rewrite pages plus the audit ledgers as of 2026-09-22; a future manuscript revision could add a Book 10 connection, which would change the verdict.
- No timeouts or source-access failures occurred in producing this ledger.

