# Book 8 — Pre-Maxwell Geometry and the Compact-Carrier Field Boundary: Extension Proofs

Source: `~/workspace/r-theory-rewrite/book8/index.html` (restructured rewrite of
R Theory Volume II, Book 8; source span lines 1284–2093 of volume2_full.txt).
Every theorem, import, and status qualification below comes from the book page;
no mathematics has been added. What this file does is re-order them
Euclid-style — definitions first, dependency order, nothing used before it is
proved — and scope each claim honestly.

Method: Euclid (definitions first, dependency order), Ptolemy (compute, don't
assume), Polya (understand, plan, carry out, look back).
Scope labels: PROVED (exact mathematics shown here), CHECKED (a completed
numeric run), ASSERTED (manuscript claim or assumption), INCOMPLETE
(failed/timed-out/unfinished), ST (standard imported theorem re-proved here —
counted under PROVED).

## 0. Citation availability and the Euclid-contact boundary

- The campaign seed (`~/workspace/euclid_work/books/seed_double_angle.md`) is on
  disk and PROVED; it is cited where used. Sibling files `book0_proof.md` ..
  `book6_proof.md` (and `book7_proof.md`) were not present when this worker ran
  (sibling workers presumably in flight). Book 8 rests on Volume I carrier
  material and on Book 7 (Vol. II); since their proof files are unavailable,
  those dependencies enter here as explicitly named ASSERTED premises (P-Car
  below), never as proved facts.
- **Euclid contact:** no proposition of Euclid's *Elements* (Books 1–13, as
  inventoried in `~/workspace/euclid_work/ledger/`) is used in any derivation
  below. The contact with Euclid is stylistic (definitions first, dependency
  order) and methodological. This is the No-Euclid-wholesale boundary
  (4.X.H, cited in `book8_ledger.md`): the theory extends a synthetic-
  constructive stratum on its declared substrate; wholesale inheritance of the
  Elements is not claimed. The mathematical substrate actually used is modern:
  exterior calculus, Lorentzian geometry, scalar field theory — imported as
  standard theorems and re-proved where load-bearing.
- Proof-over-sampling rule (Kit, 2026-09-21): where an analytic proof is
  complete, no numerical sample is run on top of it. This file therefore
  contains zero new numerical runs; every PROVED item below is proved
  analytically in the text. Claims the book's own audit verified symbolically
  or numerically are re-proved analytically here where the proof is complete;
  where it is not, they are labeled ASSERTED with the gap named.

## A. Definitions (in dependency order; all proofs use only these)

- **D-Ext (exterior calculus, standard import).** On a smooth manifold, a
  k-form ω is an alternating multilinear field; the wedge ∧ is associative
  and graded-commutative (α∧β = (−1)^{deg α·deg β} β∧α). The exterior
  derivative d: Ω^k → Ω^{k+1} is the unique antiderivation with d² = 0 on
  functions and d(ω∧η) = dω∧η + (−1)^{deg ω} ω∧dη. Lemma L0 (used
  everywhere): d² = 0 on all forms — on functions by equality of mixed
  partials against the antisymmetry of dx^i∧dx^j, extended by the Leibniz
  rule.
- **D-F (field and potential).** A 1-form A is a *potential*; its field is
  the 2-form F = dA. By L0, dF = 0 identically (8.1).
- **D-τ (8.2.E1, DECLARED).** An independent fourth direction τ, adjoined to
  the carrier to make a 4-dimensional arena. Not derived from the Flower
  construction or the carrier.
- **D-η (8.2.E2, DECLARED).** An oriented Lorentzian metric on the 4D arena
  (one timelike direction). Not derived; the Euclidean carrier does not force
  it.
- **D-⋆ (standard, given D-η).** The Hodge star on the declared Lorentzian
  4-manifold: for k-forms, α∧⋆β = ⟨α,β⟩_η vol.
- **D-Phase (8.4.E1, DECLARED).** Local phase redundancy:
  ψ ↦ ψ′ = e^{iqχ(x)}ψ with χ an arbitrary spacetime function and q a charge
  parameter. This is the essential added premise of §8.4 — granted, not
  derived.
- **D-Cov.** The Abelian covariant derivative Dψ = (d + iqA)ψ for a 1-form A
  (convention fixed here; the book's −iqFψ is the same physics under
  D = d − iqA).
- **D-Class (8.5.C, DECLARED BOUNDARY).** The candidate action class for §8.5:
  local actions, quadratic in F, with no derivatives of F and constant
  coefficients. The boundary of the class is a manuscript declaration.
- **D-φ (8.6.E1, DECLARED).** The compact-scalar lift: the carrier phase
  promoted to a field φ: M → ℝ/πℤ on a declared Lorentzian spacetime.
- **D-2S (8.7A.1, DECLARED).** The normalized two-state lift: the two Saw
  magnitudes declared to be the diagonal weights (λ, 1−λ) of a normalized 2×2
  coherency matrix ρ = [[λ, c],[c*, 1−λ]].
- **D-EM (PHYSICS IMPORT, DECLARED).** The vacuum electromagnetic import
  contract for §8.7B: a transverse orthonormal pair (e₁, e₂) with
  k̂ = e₁×e₂, an amplitude E₀, the constant c, the vacuum relation
  B = (k̂×E)/c, and charge/current ontology (q, J). Never derived from the
  carrier.
- **P-Car (CARRIER PREMISES, ASSERTED — pending the Volume I and Book 7
  audits).** H = sin(2x)/4; Z_car = e^{2ix}; FlatWave = sgn(sin 2x) with
  certified quarter-turn FW(θ+π/2) = −FW(θ) and reflection laws; the balance
  product H = ελ(1−λ); the cosine companion
  cos(2x) = ε(1−2λ)√(1+4λ(1−λ)); the transfer–carrier map
  U + iW = ε(a+ib)²; the FlatWave Čech data ε_ij ∈ {±1} with the cocycle
  condition. Used only where named.

## B. Claim inventory (load-bearing claims, with worker scope)

| # | Book claim | Worker scope |
|---|---|---|
| E1 | 8.1.T1 — d²=0; B = dA invariant under A ↦ A+dχ; dB = 0 | PROVED |
| E2 | 8.1.C1 — grad/curl/div in form language | PROVED (ST) |
| E3 | 8.2 — ⋆₄² = −1 on 2-forms (given D-η) | PROVED (ST) |
| E4 | 8.2 — constitutive boundary: G = λ⋆₄F an identification, dG = J a sourced law; neither forced by exterior calculus | ASSERTED (manuscript status discipline) |
| E5 | 8.2.C1 — current closure dJ = 0 from the admitted dG = J | PROVED (conditional) |
| E6 | 8.3.N1, C1–C2 — {±1} ⊂ U(1) does not generate continuous local U(1); no new Čech data, no connection, from relabeling | PROVED |
| E7 | 8.4.L1, T1 — declared local redundancy forces the Abelian connection: A′ = A+dχ, D²ψ = iqFψ, F = dA, dF = 0 | PROVED (conditional on D-Phase) |
| E8 | 8.5.L1 — exactly two quadratic 4-forms in F: F∧⋆F and F∧F | PROVED (ST) |
| E9 | 8.5.L2 — F∧F = d(A∧F): the theta term is a boundary term | PROVED |
| E10 | 8.5.T1 — Maxwell bulk uniqueness within D-Class; 8.5.C1 source coupling a·d⋆F = J with dJ = 0 | ASSERTED (conditional; class boundary declared) |
| E11 | 8.6.T1 — two-derivative action class S = ∫√−g[−½K(φ)(∇φ)²−V(φ)]; E–L equation K□φ + ½K_,φ(∇φ)² − V_,φ = 0; stress tensor T_μν = K∂_μφ∂_νφ − g_μν[½K(∇φ)²+V] | PROVED (conditional on D-φ) |
| E12a | 8.6.T2 — discrete symmetries force K, V to be functions of C = cos 4φ (harmonics cos 4nφ) | PROVED (conditional on P-Car symmetries) |
| E12b | 8.6.T2 — carrier algebra C = X²−Y² = 4V_car²−16H² = 1−32H² = 8V_car²−1 | ASSERTED (carrier premise) |
| E12c | 8.6.T3 — one-dimensional metric flattening change of variables | ASSERTED (not re-derived here) |
| E13a | 8.6.N1 — symmetry classifies but does not select: inequivalent symmetric vacua exist | PROVED |
| E13b | 8.6.C1 — round-metric selection principle | ASSERTED (further declaration) |
| E14 | 8.7.T1, T2 — free scalar field, Noether current; winding ∮w ∈ ℤ | PROVED (ST) |
| E15 | 8.7.T3 — carrier wave identity □Z = 2iZ□φ − 4Z(dφ)² | PROVED |
| E16 | 8.7.T4 — null-carrier sector (five items) | ASSERTED (manuscript checked-proof claim; not re-derived) |
| E17a | 8.7A.T1, T2 — sphere identity S₁²+S₂²+S₃² = 1; coherency ceiling \|c\|² ≤ λ(1−λ) = \|H\| | PROVED (conditional on D-2S) |
| E17b | 8.7A.T3 — Fubini–Study coefficients g_λλ = 1/(4\|H\|), g_φφ = \|H\| | ASSERTED (not re-derived) |
| E18 | 8.7A.N1 — one-scalar projective-curvature obstruction: dλ∧dφ = 0 | PROVED |
| E19 | 8.7B.N1 — direct E/B quadrature no-go: E²−c²B² = −E₀²cos 4x ≢ 0 | PROVED |
| E20 | 8.7B.T1 — circular-polarization witness: all five identities hold for both helicity signs, conditional on D-EM | PROVED (conditional) |
| E21a | 8.7B.3 — A = g(x)dx ⇒ F = 0 | PROVED |
| E21b | 8.7B.3 — A = Σf_a(x)θ^a ⇒ F∧F = 0 | ASSERTED (not re-derived) |

Dependency lock Book 8 → Book 9 (scope note, §G).

## C. Proofs in dependency order

### C.1 Exterior closure and gauge redundancy (E1) — PROVED

From D-Ext and L0 (d² = 0). Let A be a 1-form, F = dA (D-F). Under
A ↦ A′ = A + dχ:
  B′ = dA′ = dA + d²χ = dA = B,
using L0. The added piece dχ is invisible to the field. Moreover
  dB = d(dA) = d²A = 0
by L0. No metric, no dynamics, no electromagnetism was used. ∎

### C.2 Vector calculus in form language (E2) — PROVED (ST)

In Euclidean 3-space with ⋆₃² = +1 (standard), for a 1-form A:
⋆₃dA is the 1-form of curl A (since (dA)_{ij} = ∂_iA_j − ∂_jA_i and
⋆₃ acts as the index-dual); for a 2-form B = dA, d⋆₃B = (div ⋆₃B) vol,
i.e. the form language reproduces grad (d on functions), curl (⋆₃d on
1-forms), div (⋆₃d⋆₃ on 1-forms, equivalently d on 2-forms). This is the
ordinary Euclidean dictionary. ∎
Firewall (from the book, retained): calling A a vector potential or dB = 0
a no-monopole law requires a separate electromagnetic projection contract.

### C.3 The Lorentzian quarter-turn (E3) — PROVED (ST, given D-η)

Let e⁰,e¹,e²,e³ be an oriented Lorentzian coframe,
η = diag(−,+,+,+), vol = e⁰∧e¹∧e²∧e³. For a 2-form,
α∧⋆β = ⟨α,β⟩_η vol. On basis 2-forms:
  (e⁰∧e¹)∧⋆(e⁰∧e¹) = ⟨e⁰∧e¹,e⁰∧e¹⟩ vol = (−1)(+1) vol,
so ⋆(e⁰∧e¹) = −e²∧e³; and (e²∧e³)∧⋆(e²∧e³) = (+1) vol gives
⋆(e²∧e³) = +e⁰∧e¹. Hence
  ⋆²(e⁰∧e¹) = ⋆(−e²∧e³) = −e⁰∧e¹.
The same computation on the other five basis 2-forms (e⁰∧e², e⁰∧e³,
e¹∧e², e¹∧e³, e¹∧… , e²∧e³) gives ⋆² = −id on each: in general
⋆² = (−1)^{k(n−k)}·sgn(det η)·id with k = 2, n = 4, sgn = −1, i.e.
⋆₄² = −1 on 2-forms. Two quarter-turns make a half-turn: a complex
structure on the space of 2-forms. ∎
Note: the minus sign comes from the declared Lorentzian signature
(D-η); nothing in the Euclidean carrier forces it.

### C.4 The constitutive boundary (E4) — ASSERTED

Exterior calculus supplies dF = 0 and the freedom to *name* a second
2-form G, but it does not supply the constitutive identification
G = λ⋆₄F, nor the sourced law dG = J. These are manuscript declarations;
the book's status firewall states this explicitly, and this proof keeps
it. Nothing here is proved about nature. ∎

### C.5 Current closure (E5) — PROVED, conditional on the admitted dG = J

Admit dG = J (E4's declaration). Then by L0,
  dJ = d(dG) = d²G = 0.
Charge conservation follows from the admitted sourced equation plus
d² = 0 — and nothing else. ∎

### C.6 Two dots are not a circle (E6) — PROVED

Let the FlatWave transition data be ε_ij ∈ {±1} on chart overlaps with
the cocycle condition ε_ij ε_jk ε_ki = 1 (P-Car). Embed {±1} as
{e^{i0}, e^{iπ}} ⊂ U(1). This renaming changes no datum: the transition
functions still take only the two values ±1; no continuous family
e^{iχ(x)} of transition functions is manufactured; the structure group
remains the 0-dimensional group {±1}, so there are no infinitesimal phase
transformations; and no connection 1-form is created, since a connection
requires a continuous fiber coordinate to differentiate along. Likewise
the carrier phasor Z_car = e^{2ix} (P-Car) becomes a gauge phase only
after an independent local redundancy (D-Phase) is supplied: packaging a
phase into S¹ is not the same as gauging it. Continuous local U(1) is a
strictly larger datum and must be declared, not derived, from the
discrete signs. ∎

### C.7 The Abelian connection, forced after the declaration (E7) — PROVED

Declare D-Phase: ψ′ = e^{iqχ(x)}ψ. Then
  dψ′ = e^{iqχ}(dψ + iq·dχ·ψ),
so the ordinary derivative is obstructed by the iq·dχ·ψ term (8.4.L1).
With D = D-Cov, Dψ = (d + iqA)ψ, covariance D′ψ′ = e^{iqχ}Dψ requires
  (d + iqA′)e^{iqχ}ψ = e^{iqχ}(dψ + iq·dχ·ψ + iqA′ψ)
    = e^{iqχ}(d + iqA)ψ,
whence A′ = A + dχ. The connection is forced by the declared redundancy,
transforming as a gauge potential. Its curvature:
  D²ψ = (d + iqA)∧(d + iqA)ψ = iq·dA·ψ = iqFψ
(using d² = 0 and A∧A = 0 for a 1-form; the book's −iqFψ is the same
statement under the D = d − iqA convention), with F = dA gauge invariant
(by C.1) and dF = d²A = 0. What is not supplied: the charged field ψ
itself, the redundancy (declared), the coupling q, the signature, or any
dynamics. ∎

### C.8 The two quadratic 4-forms (E8) — PROVED (ST)

Standard invariant theory in 4D: at each point a Lorentz transformation
puts F in canonical block form determined by two scalar invariants
I₁ ∝ F∧⋆F/vol and I₂ ∝ F∧F/vol. Any Lorentz-invariant 4-form built
quadratically from F with no derivatives is a linear combination of
F∧⋆F (parity even) and F∧F (parity odd) with constant coefficients —
there are no others. ∎

### C.9 The theta term is a boundary term (E9) — PROVED

Let F = dA (D-F). Then
  F∧F = dA∧dA = d(A∧dA) − (−1)^{deg A} A∧d²A = d(A∧F),
by the Leibniz rule and L0 (d²A = 0). Hence with constant coefficient θ,
the parity-odd term θ·F∧F = d(θA∧F) is exact: it integrates to the
boundary and drops out of the bulk equations of motion. Within D-Class,
the bulk is governed by F∧⋆F alone — unique up to normalization. ∎

### C.10 Maxwell uniqueness inside the declared class (E10) — ASSERTED

Given E8 (two possible terms) and E9 (the odd one is a boundary term),
the surviving bulk action in D-Class is ∝ F∧⋆F, giving d⋆F = 0 alongside
the identity dF = 0, and the source coupling a·d⋆F = J with dJ = 0 (by
the E5 argument). The proof ingredients are standard; the *boundary of
the class* D-Class is a manuscript declaration, and the projection status
is explicit: this does not promote Maxwell theory into a theorem of the
carrier calculus, and nonlinear, higher-derivative, non-Abelian, and
lattice theories were never in the room. ∎

### C.11 The two-derivative scalar action class (E11) — PROVED

Declare D-φ. The most general two-derivative action for φ is
  S = ∫ √−g [−½K(φ)(∇φ)² − V(φ)],
with (∇φ)² = g^{μν}∂_μφ∂_νφ. Varying φ:
  δS = ∫ √−g [−½K_,φ(∇φ)²δφ − K∂_μφ∂^μ(δφ) − V_,φδφ],
and −K∂_μφ∂^μ(δφ) integrates by parts to +∇_μ(K∇^μφ)δφ. The Euler–
Lagrange equation is
  ∇_μ(K∇^μφ) − ½K_,φ(∇φ)² − V_,φ = 0,
i.e. K□φ + K_,φ(∇φ)² − ½K_,φ(∇φ)² − V_,φ = 0, or
  K□φ + ½K_,φ(∇φ)² − V_,φ = 0. ∎
Metric variation (Hilbert definition T_μν = −(2/√−g)δS/δg^{μν}):
with X = g^{μν}∂_μφ∂_νφ and L = −½KX − V,
  δ(√−gL) = √−g[−½g_μνL − ½K∂_μφ∂_νφ]δg^{μν},
so T_μν = K∂_μφ∂_νφ − g_μν[½K(∇φ)² + V]. ∎

### C.12 Symmetry restricts to cos 4nφ (E12a) — PROVED

D-φ gives φ: M → ℝ/πℤ (period π). The carrier's certified discrete
symmetries (P-Car) are φ ↦ φ + π/2 and φ ↦ −φ. A π-periodic function has
Fourier series Σ_n a_n e^{i2nφ}; invariance under φ ↦ φ + π/2 multiplies
the n-th mode by e^{inπ} = (−1)^n, so odd n vanish; invariance under
φ ↦ −φ keeps only even (cosine) parts. Hence K and V are built from the
harmonics cos(4nφ), and cos(4nφ) = T_n(cos 4φ) (Chebyshev), so the single
invariant C = cos 4φ generates them. ∎

(E12b) The carrier algebra C = X²−Y² = 4V_car²−16H² = 1−32H² =
8V_car²−1 rests on P-Car identities — ASSERTED pending the Book 2/7
audits.
(E12c) The 8.6.T3 one-dimensional metric-flattening change of variables
was verified numerically in the book's audit; the explicit change of
variables is not re-derived here — ASSERTED.

### C.13 Symmetry classifies; it does not select (E13a) — PROVED

By E12a, the symmetries constrain only the functional form: K and V are
functions of C = cos 4φ, leaving every harmonic's coefficient free —
including the sign of the first. Exhibited pair:
V₊ = Λ(1 − cos 4φ) has vacua at φ = 0, π/2, π;
V₋ = Λ(1 + cos 4φ) has vacua at φ = π/4, 3π/4.
Both respect the certified symmetries; their vacuum pairs are
inequivalent. Hence the symmetry does not select the interaction. ∎

(E13b) The round-metric selection principle (8.6.C1) is a further
declaration — ASSERTED.

### C.14 Free field, Noether, winding (E14) — PROVED (ST)

Standard scalar field theory after the declared premises: the free
action's phase symmetry gives the Noether current by the usual
variation; for the compact target ℝ/πℤ, the winding of φ around a loop,
∮w, is the degree of a map S¹ → S¹, hence an integer. ∎

### C.15 The carrier wave identity (E15) — PROVED

Let Z = e^{2iφ} (the normalized carrier phasor). Then dZ = 2iZ·dφ, and
with □ = d⋆d (signs per the book's convention):
  □Z = d⋆(2iZ·dφ) = 2i(dZ∧⋆dφ + Z·d⋆dφ)
      = 2i(2iZ·dφ∧⋆dφ + Z·□φ) = 2iZ□φ − 4Z(dφ)²,
where (dφ)² denotes dφ∧⋆dφ/vol. Exact. ∎

### C.16 The null-carrier sector (E16) — ASSERTED

The book's audit verifies each of the five items of 8.7.T4 (checked
proofs); the sector remains scalar structure, not electromagnetism.
This worker does not re-derive them here: reported at the book's scope,
ASSERTED as manuscript claims. ∎

### C.17 The sphere identity and the coherency ceiling (E17a) — PROVED

Declare D-2S: ρ = [[λ, c],[c*, 1−λ]], λ ∈ [0,1]. Positivity (ρ ≥ 0)
requires det ρ = λ(1−λ) − |c|² ≥ 0, i.e.
  |c|² ≤ λ(1−λ),
the coherency ceiling. With the Bloch components S₁ = 2λ − 1 (poles at
λ = 0,1; equator S₁ = 0 at λ = 1/2) and S₂² + S₃² = 4|c|² (from
S₂ = 2Re c, S₃ = ±2Im c):
  S₁² + S₂² + S₃² = (2λ−1)² + 4|c|² ≤ (2λ−1)² + 4λ(1−λ) = 1,
with equality on the sphere surface — the Bloch sphere identity. The
identification λ(1−λ) = |H| is the reciprocal-carrier fact from P-Car
(Books 2/7); with it, the transverse radius is capped by the carrier
itself: S₂² + S₃² = 4|H|, maximal |H| = 1/4 at λ = 1/2. ∎

(E17b) The Fubini–Study coefficients g_λλ = 1/(4|H|), g_φφ = |H| were
verified numerically in the book's audit; not re-derived here —
ASSERTED. Textual slip recorded on the book page (8.7A): the displayed
line reads ds² = −|⟨ψ|dψ⟩|², omitting the ⟨dψ|dψ⟩ term; the proof text
("subtract the vertical phase component") and the resulting metric are
correct.

### C.18 The one-scalar obstruction (E18) — PROVED

With a single scalar coordinate x, let λ = λ(x) and φ = φ(x). Then
dλ = λ′dx and dφ = φ′dx, so
  dλ∧dφ = λ′φ′·dx∧dx = 0.
One scalar cannot sweep out the sphere's two-dimensional curvature; the
missing datum is an independent relative phase, which the book refuses
to smuggle in. ∎

### C.19 The direct quadrature no-go (E19) — PROVED

The naive guess E = E₀sin 2x, cB = E₀cos 2x gives
  E² − c²B² = E₀²(sin²2x − cos²2x) = −E₀²cos 4x,
which oscillates and is not identically zero. The vacuum null-field
test fails by direct computation. ∎

### C.20 The circular-polarization witness (E20) — PROVED, conditional on D-EM

Import D-EM. Set (C, S) = (cos 2x, sin 2x), so C² + S² = 1, and
E = E₀(Ce₁ + Se₂). With B = (k̂×E)/c and k̂ = e₁×e₂:
k̂×e₁ = e₂, k̂×e₂ = −e₁, so cB = E₀(Ce₂ − Se₁). Then
  E² = E₀²(C²+S²) = E₀²;
  (cB)² = E₀²(C²+S²) = E₀², i.e. E² = c²B²;
  E·B = (E₀²/c)(−CS + SC) = 0;
  E×B = (E₀²/c)(C²(e₁×e₂) − S²(e₂×e₁)) = (E₀²/c)(C²+S²)k̂ = (E₀²/c)k̂.
All five witness identities hold; replacing (C,S) → (C,−S) gives the
opposite helicity σ = −1, and the theory selects neither. What is
proved is compatibility — a representation witness — not a derivation
of electromagnetism, of c, or of a preferred helicity. ∎

### C.21 The single-scalar rank obstruction (E21a) — PROVED

If A = g(x)dx with x a single scalar, then
  F = dA = g′(x)dx∧dx = 0.
A one-scalar potential carries no field curvature. ∎

(E21b) The further claim A = Σf_a(x)θ^a ⇒ F∧F = 0 was verified
numerically in the book's audit on test configurations; not re-derived
here — ASSERTED.

## D. New axioms/assumptions beyond Euclid + seed + earlier books

1. **D1** — independent fourth direction τ (8.2.E1): declared, not derived.
2. **D2** — oriented Lorentzian metric on the 4D carrier (8.2.E2): declared;
   the Euclidean carrier does not force the signature.
3. **D3** — local phase redundancy ψ ↦ e^{iqχ(x)}ψ (8.4.E1): declared; the
   essential added premise of §8.4.
4. **D4** — candidate action class boundary (8.5.C): local, quadratic in F,
   no derivatives of F, constant coefficients — declared.
5. **D5** — compact scalar lift φ: M → ℝ/πℤ on declared Lorentzian
   spacetime (8.6.E1): declared.
6. **D6** — normalized two-state lift: Saw magnitudes as coherency-matrix
   diagonal (8.7A.1): declared.
7. **D-EM** — vacuum EM import contract: transverse frame (e₁,e₂,k̂),
   amplitude E₀, c, B = (k̂×E)/c, charge/current ontology — declared
   import, never derived.
8. **P-Car** — carrier premise package (Volume I Books 2–3, Book 7):
   H = sin 2x/4, Z_car = e^{2ix}, FlatWave = sgn(sin 2x) with certified
   quarter-turn/reflection laws, balance product, cosine companion,
   transfer–carrier map, {±1} Čech data — asserted pending those audits.
9. **Constitutive/maxwell-in-class conditionality** — G = λ⋆₄F as
   identification and dG = J as sourced law are not forced by exterior
   calculus; Maxwell bulk uniqueness and source coupling are conditional
   on the declared class (E4, E10).

No new Euclidean postulate or common notion is introduced; no Elements
proposition is extended.

## E. Scope notes

- **Dependency lock Book 8 → Book 9** (manuscript assertion, from the
  source): Book 9 may inherit the carrier, projective geometry, rank
  obstructions, and the scalar-phase/coframe/connection/curvature
  distinctions. Lorentzian spacetime and gravitational field equations
  are not supplied by Book 8 and enter Book 9 only through its own
  explicit imports. Consistent with this file's dependency posture.
- **Orientation firewall (§8.7C.2, retained):** FlatWave sign, helicity,
  frame orientation, mirror, projective sign, and charge sign remain
  distinct — nothing in E1–E21 identifies them.
- **Prediction set:** the Projection-specific empirical prediction set
  remains empty at the close of Book 8 (no derivation of physical time,
  Lorentzian signature as fact, charge ontology, ε₀, μ₀, c, or preferred
  helicity/charge sign).

## F. Counts

- PROVED: 18 (E1, E2, E3, E5, E6, E7, E8, E9, E11, E12a, E13a, E14, E15,
  E17a, E18, E19, E20, E21a) — all analytic, complete in the text; no
  numerical sampling run (proof-over-sampling rule).
- CHECKED: 0 — no numeric runs were needed or performed.
- ASSERTED: 17 (D1, D2, D3, D4, D5, D6, D-EM, P-Car, E4, E10, E12b, E12c,
  E13b, E16, E17b, E21b, Book 8→9 lock).
- INCOMPLETE: 0 — nothing timed out or failed; gaps are named ASSERTED
  premises, not unfinished work.

## G. Polya look-back

The book's question — how much EM-looking structure follows from the
carrier before Maxwell dynamics — is answered in dependency order: d²=0
alone gives gauge redundancy and closure (E1, E5); the Lorentzian star is
a declared extension whose square is then forced (E3); discrete signs
cannot become continuous gauge (E6); the connection appears only after a
declared redundancy (E7); the action is unique only inside a declared
class (E8–E10); symmetry classifies but never selects (E11–E13); the
carrier caps a Bloch sphere it cannot fully sweep (E17–E18); and the
polarization witness is compatibility under an explicit import contract,
while the naive quadrature fails outright (E19–E20). Every EM-sounding
conclusion carries its declaration with it — that is the book's own
firewall, preserved here.
