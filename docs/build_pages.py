#!/usr/bin/env python3
"""Build the Euclid proof-campaign book webpages (Books 21, 22).

Reads the claim data below (transcribed from trig_proof/book21_claims.md
and trig_proof/book22_claims.md, 2026-09-26) and emits docs/index.html,
docs/book21/index.html, docs/book22/index.html plus docs/style.css.
Run: python3 docs/build_pages.py
"""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))

CSS = """\
:root {
  --ink: #1a1a2e; --muted: #5b5b6e; --paper: #faf9f6; --card: #ffffff;
  --line: #e4e1d8; --proved: #1e7e34; --checked: #b7791f; --asserted: #6c757d;
  --incomplete: #c0392b; --accent: #2c3e70;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--paper); color: var(--ink);
  font-family: Georgia, 'Times New Roman', serif; line-height: 1.65; }
.wrap { max-width: 860px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem; }
.eyebrow { font-family: -apple-system, 'Segoe UI', sans-serif; font-size: .78rem;
  letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }
h1 { font-size: 2rem; line-height: 1.25; margin: .4rem 0 .2rem; }
.sub { color: var(--muted); font-style: italic; margin: 0 0 1.5rem; }
.meta { background: var(--card); border: 1px solid var(--line); border-radius: 10px;
  padding: 1rem 1.25rem; font-size: .95rem; margin-bottom: 1.5rem; }
.meta dt { font-family: -apple-system, 'Segoe UI', sans-serif; font-size: .75rem;
  letter-spacing: .08em; text-transform: uppercase; color: var(--muted);
  margin-top: .6rem; }
.meta dt:first-child { margin-top: 0; }
.meta dd { margin: .15rem 0 0; }
.counts { display: flex; flex-wrap: wrap; gap: .6rem; margin: 1.25rem 0; }
.count { font-family: -apple-system, 'Segoe UI', sans-serif; font-size: .85rem;
  background: var(--card); border: 1px solid var(--line); border-radius: 999px;
  padding: .3rem .9rem; }
.count b { font-size: 1rem; }
.badge { display: inline-block; font-family: -apple-system, 'Segoe UI', sans-serif;
  font-size: .72rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase;
  border-radius: 6px; padding: .22rem .6rem; color: #fff; vertical-align: middle; }
.badge.proved { background: var(--proved); }
.badge.checked { background: var(--checked); }
.badge.asserted { background: var(--asserted); }
.badge.incomplete { background: var(--incomplete); }
.claim { background: var(--card); border: 1px solid var(--line); border-radius: 10px;
  padding: 1.1rem 1.25rem; margin: 0 0 1rem; }
.claim-head { display: flex; align-items: baseline; gap: .7rem; flex-wrap: wrap;
  margin-bottom: .5rem; }
.claim-id { font-family: -apple-system, 'Segoe UI', sans-serif; font-weight: 700;
  font-size: 1rem; color: var(--accent); }
.claim-text { margin: .4rem 0; }
.claim dl { margin: .7rem 0 0; font-size: .92rem; }
.claim dt { font-family: -apple-system, 'Segoe UI', sans-serif; font-size: .72rem;
  letter-spacing: .08em; text-transform: uppercase; color: var(--muted);
  margin-top: .55rem; }
.claim dd { margin: .15rem 0 0; }
.note { border-left: 3px solid var(--line); padding-left: .8rem; color: #33333f; }
footer { margin-top: 2.5rem; padding-top: 1.25rem; border-top: 1px solid var(--line);
  font-family: -apple-system, 'Segoe UI', sans-serif; font-size: .85rem; color: var(--muted); }
footer a { color: var(--accent); }
a { color: var(--accent); }
.booklink { display: block; background: var(--card); border: 1px solid var(--line);
  border-radius: 10px; padding: 1.25rem 1.4rem; margin: 0 0 1rem; text-decoration: none;
  color: var(--ink); }
.booklink:hover { border-color: var(--accent); }
.booklink h2 { margin: 0 0 .3rem; font-size: 1.3rem; }
.booklink p { margin: .2rem 0 0; color: var(--muted); font-size: .95rem; }
"""

def badge(verdict):
    v = verdict.upper()
    cls = "proved" if v.startswith("PROVED") else \
          "checked" if v.startswith("CHECKED") else \
          "incomplete" if v.startswith("INCOMPLETE") else "asserted"
    return f'<span class="badge {cls}">{html.escape(verdict)}</span>'

def claim_card(c):
    rows = []
    rows.append(f'<div class="claim-head"><span class="claim-id">{html.escape(c["id"])}</span>{badge(c["verdict"])}</div>')
    rows.append(f'<p class="claim-text">{html.escape(c["claim"])}</p>')
    rows.append('<dl>')
    rows.append(f'<dt>Scope</dt><dd>{html.escape(c["scope"])}</dd>')
    rows.append(f'<dt>Folded into a principle?</dt><dd>{html.escape(c["folded"])}</dd>')
    if c["notes"].strip() not in ("", "—"):
        rows.append(f'<dt>Verification notes</dt><dd class="note">{html.escape(c["notes"])}</dd>')
    rows.append('</dl>')
    return '<article class="claim">\n' + "\n".join(rows) + '\n</article>'

def book_page(book):
    counts = " · ".join(
        f'<span class="count"><b>{n}</b> {k}</span>'
        for k, n in book["counts"])
    cards = "\n".join(claim_card(c) for c in book["claims"])
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(book["title"])} — Euclid Proof Campaign</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>
<div class="wrap">
<p class="eyebrow">Euclid Proof Campaign · Book {book["n"]}</p>
<h1>{html.escape(book["title"])}</h1>
<p class="sub">{html.escape(book["subtitle"])}</p>

<div class="meta">
<dl>
<dt>Source</dt><dd>{html.escape(book["source"])}</dd>
<dt>Evaluated</dt><dd>{html.escape(book["evaluated"])}</dd>
<dt>Euclid boundary</dt><dd>{html.escape(book["boundary"])}</dd>
<dt>Status</dt><dd><span class="badge proved">complete</span></dd>
</dl>
</div>

<div class="counts">{counts}</div>

<p><strong>New principles folded: {book["new_principles"]}.</strong> {html.escape(book["new_principles_note"])}</p>
{f'<p>{html.escape(book["standing"])} </p>' if book.get("standing") else ""}

<h2>Claim-by-claim evaluation</h2>
{cards}

<footer>
<p><a href="../index.html">← All book pages</a> · Full evaluation tables:
<a href="https://github.com/cosbykit-afk/euclid-proofs/blob/master/trig_proof/book{book["n"]}_claims.md">trig_proof/book{book["n"]}_claims.md</a></p>
<p>Verdicts follow the campaign's status grammar: PROVED (complete proof),
CHECKED (completed computation or cited recomputation), ASSERTED (declared,
imported, or methodological), INCOMPLETE (unfinished). Nothing here is rounded
up or down.</p>
</footer>
</div>
</body>
</html>
"""

INDEX = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Euclid Proof Campaign — Book webpages</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">
<p class="eyebrow">Euclid Proof Campaign</p>
<h1>Book webpages</h1>
<p class="sub">Claim-by-claim proof evaluations, published as readable pages.</p>
<a class="booklink" href="book21/">
<h2>Book 21 — Fermion Composition, Color Closure, and Bound-State Geometry</h2>
<p>13 claims evaluated 2026-09-26: 6 PROVED · 2 CHECKED · 5 ASSERTED · 0 INCOMPLETE. No new principles.</p>
</a>
<a class="booklink" href="book22/">
<h2>Book 22 — Canonical Spin–Geometry and the Primitive Symplectic Atlas</h2>
<p>10 claims evaluated 2026-09-26: 7 PROVED · 0 CHECKED · 3 ASSERTED · 0 INCOMPLETE. No new principles.</p>
</a>
<footer>
<p>Source of truth: the <a href="https://github.com/cosbykit-afk/euclid-proofs">euclid-proofs</a>
repository (<code>trig_proof/</code>). Pages are generated by
<code>docs/build_pages.py</code> from the evaluated claim tables.</p>
</footer>
</div>
</body>
</html>
"""

# ---------------------------------------------------------------- data ----
book21 = {
    "n": 21,
    "title": "Book 21 — Fermion Composition, Color Closure, and Bound-State Geometry",
    "subtitle": "Volume 0. Claim-by-claim proof evaluation.",
    "source": "Rewrite page r-theory-rewrite/book21/index.html (principal theorems). No book21_proof.md exists (the earlier campaign covered Books 0–20 only); every claim is sourced from the rewrite page, restated and verified from the page's content.",
    "evaluated": "2026-09-26",
    "boundary": "No proposition of Euclid's Elements is a premise of any claim below (the page invokes none; the only \u201cEuclidean\u201d occurrence is the phrase \u201cEuclidean metric\u201d for the A\u2082 realization layer). No ledger verification was therefore required.",
    "counts": [("evaluated", 13), ("PROVED", 6), ("CHECKED", 2), ("ASSERTED", 5), ("INCOMPLETE", 0)],
    "new_principles": "0",
    "new_principles_note": "Every claim with trigonometric content is a corollary or restatement of already-registered principles (P17, P19, P30, P49, P51); the rest is Lie algebra, representation theory, analysis, empirics, imports, or negatives.",
    "claims": [
        {"id": "B21.1", "verdict": "PROVED", "claim": "Composition firewall: Sym(V_A\u2297V_B) = [Sym(V_A)\u2297Sym(V_B)] \u2295 [Alt(V_A)\u2297Alt(V_B)]; locally visible subsystem coordinates need not determine the full composite state.",
         "scope": "PROVED", "folded": "No \u2014 linear algebra, not a trig identity",
         "notes": "Verified by dimension count: both sides have dimension mn(mn+1)/2 for dim V_A=m, dim V_B=n; the two summands are orthogonal subspaces of the symmetric sector."},
        {"id": "B21.2a", "verdict": "ASSERTED", "claim": "Declared extension V\u2083 = \u2102\u00b3 (not derived from Book 0).",
         "scope": "ASSERTED", "folded": "No \u2014 declaration",
         "notes": "The book labels it DECLARED itself; a declaration cannot found a principle."},
        {"id": "B21.2b", "verdict": "PROVED", "claim": "Three-state closure: from declared V\u2083, centered weights form an equilateral triangle in the sum-zero plane; pairwise differences give the A\u2082 root system (Cartan [[2,\u22121],[\u22121,2]], six roots, regular hexagon); one su(2) + one bridge closes to su(3) (minimal within the declared candidate class); the tetrahedral metric G=\u00bd(I+J) restricts to a scalar multiple of the Euclidean metric on the A\u2082 plane (compatible, not foundational).",
         "scope": "PROVED (given the declared V\u2083)", "folded": "No \u2014 Lie algebra / root-system geometry, not a trig identity",
         "notes": "Standard: weights e_i \u2212 \u2153\u03a3e_j, differences e_i\u2212e_j = 6 roots; simple roots generate su(3). The weight angles (30\u00b0, 150\u00b0, 270\u00b0) are representation coordinates, firewalled by the book itself as non-spatial."},
        {"id": "B21.3", "verdict": "PROVED", "claim": "Triadic color closure, conditional on the QCD import: 3\u22973\u0304 = 1\u22958, 3\u22973\u22973 = 1\u22958\u22958\u229510, \u03b5-contraction exactly color-invariant; color/anticolor hexagon interlaces the root hexagon at an exact 30\u00b0 offset. Obstruction kept: singlet representation theory does not derive confinement, couplings, or a Hamiltonian.",
         "scope": "PROVED-conditional (asserted QCD import: quarks in 3, antiquarks in 3\u0304, gluons in 8, su(3) connection, plus the V\u2083\u2194color-carrier projection contract)", "folded": "No \u2014 representation theory, not a trig identity",
         "notes": "Dimension checks: 3\u00b73 = 9 = 1+8; 27 = 1+8+8+10. The obstruction is a retained negative about what the exhibited tensors prove."},
        {"id": "B21.4", "verdict": "PROVED", "claim": "Two-fermion invariant: from supplied masses and ordinary special relativity, s = 2m\u2081m\u2082(cosh \u03bb_m + cosh \u03b7) with \u03bb_m = ln(m\u2081/m\u2082), q_m = tanh(\u03bb_m/2), q_v = tanh(\u03b7/2); equivalently s/(m\u2081m\u2082) = [R(q_m)+R(q_m)\u207b\u00b9] + [R(q_v)+R(q_v)\u207b\u00b9], R(q) = (1+q)/(1\u2212q). Guards: q_m, q_v are independent physical data; m\u2081/m\u2082 = R(q_m) is a coordinate change, not a mass-generation mechanism.",
         "scope": "PROVED (exact; SR is background physics, masses supplied)", "folded": "No \u2014 trig kernel already registered",
         "notes": "R(q) = (1+q)/(1\u2212q) is P30's M\u00f6bius map Q\u208a in the q variable; R(q)+R(q)\u207b\u00b9 = 2(1+q\u00b2)/(1\u2212q\u00b2) = 2cosh \u03bb_m is a two-line corollary of P49; hence s/(2m\u2081m\u2082) = cosh \u03bb_m + cosh \u03b7 is exactly P51's premise form. Nothing new. Sanity: 2m\u2081m\u2082cosh \u03bb_m = m\u2081\u00b2+m\u2082\u00b2, so s = m\u2081\u00b2+m\u2082\u00b2+2m\u2081m\u2082cosh \u03b7 is the standard 1+1 invariant."},
        {"id": "B21.5", "verdict": "PROVED", "claim": "Bound-mass coordinate: on the declared analytic branch \u03b7 \u2192 i\u03b8, u = tan(\u03b8/2), u\u00b2 = [(m\u2081+m\u2082)\u00b2\u2212M\u00b2]/[M\u00b2\u2212(m\u2081\u2212m\u2082)\u00b2], M\u00b2 = (m\u2081\u2212m\u2082)\u00b2 + 4m\u2081m\u2082/(1+u\u00b2); weak binding u\u00b2 = B/(2\u03bc) + O(B\u00b2); heavy-source limit u\u00b2 \u2192 (m\u2082\u2212E)/(m\u2082+E).",
         "scope": "PROVED (exact algebra; the expansion/limit are analysis)", "folded": "No \u2014 u = tan(\u03b8/2) is P19's Weierstrass form; the rest is algebra/analysis, not a trig identity",
         "notes": "Verified: the two displayed forms are equivalent (cross-multiplication gives 4m\u2081m\u2082 + (m\u2081\u2212m\u2082)\u00b2 = (m\u2081+m\u2082)\u00b2); the weak-binding expansion and the m\u2081\u2192\u221e limit check out term by term."},
        {"id": "B21.6", "verdict": "PROVED", "claim": "Independent coordinate convergence: on the n_r = 0, \u03ba < 0 heavy-source circular branch of the imported Dirac\u2013Coulomb theory, |G/F|\u00b2 = (m\u2212E)/(m+E), so u_pair = |G/F| = sxp(x) exactly, from two independent routes with no fitted mass ratio. The n_r > 0 obstruction (ratio runs with radius; one global u cannot reconstruct a generic excited radial spinor) is part of the theorem.",
         "scope": "PROVED-conditional (asserted imports: point-Coulomb Dirac equation; radial Dirac\u2013Coulomb paper's circular-state theorem; declared state family)", "folded": "No \u2014 trig content is P19/P17 under the import",
         "notes": "|G/F| = tan(\u03b8/2)-type half-angle tangent is P19's Weierstrass form; sxp(x) = tan(x/2) on the sine channel is P17. The convergence is the equality of two routes, conditional on the imports \u2014 not a new trig principle."},
        {"id": "B21.7", "verdict": "CHECKED", "claim": "Verified numbers (recomputed 2026-09-19 from frozen inputs, cited): hydrogen q_m \u2248 0.99891135885, u_H(1S) \u2248 0.003648720323 with \u03b1/2 < u_H < u_C; deuteron B_d \u2248 2.22456637 MeV, q_m \u2248 0.00068873505, u_d \u2248 0.0487186123; muonium q_m \u2248 0.99037.",
         "scope": "CHECKED (cited recomputation, not re-run per proof-over-sampling discipline)", "folded": "No \u2014 empirical numbers, not a trig identity", "notes": "\u2014"},
        {"id": "B21.8a", "verdict": "CHECKED", "claim": "Frozen failure: 81/32 is not exact \u2014 R_\u03b2 = (m_n\u2212m_p)/m_e \u2248 2.53098858276 vs 81/32 = 2.53125, residual \u2248 \u2212133.6 eV.",
         "scope": "CHECKED (numerical comparison)", "folded": "No \u2014 negative result, not a trig identity",
         "notes": "Must not be presented as an exact mass formula (the book's own guard)."},
        {"id": "B21.8b", "verdict": "ASSERTED", "claim": "Other frozen failures: fifth-lattice proximity is not mass quantization; closure defects are not musical commas; the order-five mass route failed.",
         "scope": "ASSERTED (retained negatives, not re-derived here)", "folded": "No \u2014 negatives, not trig",
         "notes": "Inherited by any future flavor/mass program; may not be silently reversed."},
        {"id": "B21.9", "verdict": "ASSERTED", "claim": "Preregistration rule (constituent/bound-state/coordinate definitions, reference theory, provenance, uncertainty, \u0394_op, failure criterion before testing a mass law).",
         "scope": "ASSERTED (methodology)", "folded": "No \u2014 methodology, not a trig identity", "notes": "\u2014"},
        {"id": "B21.10", "verdict": "ASSERTED", "claim": "Higher-carrier audit (E8(\u221224)): 248-direction reconstruction, zero-residual particle/mirror matching, su(2,3)\u2295u(1)_Y centralizer, commuting SU(5) partner \u2014 cited to the project's Verification Ledger, not proved in this text; firewalled (no theorem of \u00a7\u00a71\u20137 depends on it).",
         "scope": "ASSERTED (ledger-cited)", "folded": "No \u2014 cited, not proved here",
         "notes": "Cannot be stated as established until that ledger and its code are rerun."},
        {"id": "B21.11", "verdict": "ASSERTED", "claim": "Closure audit: \u0394_op(Book 21) = \u2205; null hypothesis C0 retained; color and mass architectures logically independent.",
         "scope": "ASSERTED (the book's own conclusion)", "folded": "No \u2014 meta, not a trig identity", "notes": "\u2014"},
    ],
}

book22 = {
    "n": 22,
    "title": "Book 22 — Canonical Spin\u2013Geometry and the Primitive Symplectic Atlas",
    "subtitle": "Volume 0. Claim-by-claim proof evaluation.",
    "source": "Rewrite page r-theory-rewrite/book22/index.html (principal theorems). No book22_proof.md exists; every claim is sourced from the rewrite page, restated and verified from the page's content.",
    "evaluated": "2026-09-26",
    "boundary": "No proposition of Euclid's Elements is a premise of any claim below (the page invokes none). No ledger verification was therefore required.",
    "counts": [("evaluated", 10), ("PROVED", 7), ("CHECKED", 0), ("ASSERTED", 3), ("INCOMPLETE", 0)],
    "new_principles": "0",
    "new_principles_note": "The book's exact content is differential and symplectic geometry of the radial-spinor (F,G) phase plane (Pr\u00fcfer pair, primitive symplectic atlas with common one-form p_Q dQ = \u22122G dF + 2F dG and \u03c9_spin = 4 dF\u2227dG) plus conditional reconstructions of imported physics. No claim yields a new identity, lemma, or exact relation about trigonometric functions, angles, or circular/hyperbolic measure.",
    "standing": "Standing note: \u201cpromotion\u201d of earlier results means restriction to a specialized setting with reuse of existing proofs \u2014 a status-preserving operation, never a status upgrade and never new evidence (the book's own rule, kept).",
    "claims": [
        {"id": "B22.1", "verdict": "ASSERTED", "claim": "Imported machinery and declared contracts: radial coframe e^a (flat at \u03b7=0, defect \u03b4_e = e^0\u2212dr), torsion-free spin connection, Dirac spinor \u03a8 in the projected chart; contract C6a (radial two-component chart \u03a8 \u2192 (r,F,G,\u2026)); contract C6b (F and G independent on open sets).",
         "scope": "ASSERTED (imports + declared contracts)", "folded": "No \u2014 imports/contracts",
         "notes": "The book labels these IMPORT/declared itself."},
        {"id": "B22.2", "verdict": "PROVED", "claim": "Obstruction: the spherical-to-Cartesian map is not a global diffeomorphism (origin and polar axis excluded).",
         "scope": "PROVED (negative)", "folded": "No \u2014 differential geometry, not a trig identity",
         "notes": "Standard: the map fails injectivity/regularity at r = 0 and on the polar axis."},
        {"id": "B22.3", "verdict": "ASSERTED", "claim": "C6a/C6b fix the reading of the geometry but not the physical meaning of F and G; importing the radial Dirac\u2013Coulomb paper promotes the chart, never the book's own assumptions.",
         "scope": "ASSERTED (methodological)", "folded": "No \u2014 methodology", "notes": "\u2014"},
        {"id": "B22.4", "verdict": "PROVED", "claim": "Pr\u00fcfer canonical pair (exact conditional): the transport operator on (F,G) has exact zero trace, giving the radial invariant FF\u2032 + GG\u2032 = \u2212A\u00b2/(2r); Pr\u00fcfer angle \u0398 = arg(G+iF) and spin density A\u00b2 = F\u00b2+G\u00b2 form a canonical pair on the radial-spinor phase plane with symplectic form \u03c9_spin = 4 dF\u2227dG, regular on open sets under C6a/C6b. Obstruction kept: does not derive the Dirac equation, spin-\u00bd, spin-statistics, or \u03b1.",
         "scope": "PROVED-conditional (imported radial Dirac equations + C6a/C6b)", "folded": "No \u2014 differential geometry of the (F,G) phase plane, not a trig identity",
         "notes": "The page states the zero-trace input and the invariant as consequence; internal consistency verified: (A\u00b2)\u2032 = 2(FF\u2032+GG\u2032) = \u2212A\u00b2/r. The angle \u0398 enters only as a phase-plane coordinate; no identity about trig functions is proved."},
        {"id": "B22.5", "verdict": "PROVED", "claim": "Primitive symplectic atlas (the volume's strongest exact result): p_sxp = 2F\u00b2, p_srx = \u22122G\u00b2, p_cxp = (F\u2212G)\u00b2, p_crx = \u2212(F+G)\u00b2 are four Darboux-compatible charts on the same (F,G) plane with common one-form p_Q dQ = \u22122G dF + 2F dG and common symplectic form \u03c9_spin = 4 dF\u2227dG; chart transition identities, reciprocal relations, and amplitude-ratio readings are exact; on the circular Dirac\u2013Coulomb branch the charts cross-check the radial paper's spinor-ratio theorem.",
         "scope": "PROVED (exact internal theorem; conditional only on the declared C6a/C6b chart and the imported radial dynamics)", "folded": "No \u2014 a representation theorem in (F,G) variables, not a trig identity",
         "notes": "The \u201creciprocal/complementary identities\u201d are differential identities of the atlas charts, not identities about sin/cos/tan. The book states it changes no prediction of the imported theory."},
        {"id": "B22.6", "verdict": "PROVED", "claim": "Spherical defect reduction (conditional reconstruction): exact reduction of the imported first-order Einstein\u2013Hilbert action in the defect variables (\u03b4_e, \u03b4_f, \u03b4_\u03c9) under declared regularization \u03b7\u00b2(r)dr on (r_UV,\u221e) and asymptotically flat falloff; on-shell defect action vanishes in the massless flat defect-free limit. Obstruction kept: does not derive the Einstein field equations, Newton's constant, or the mass parameter.",
         "scope": "PROVED-conditional (imported first-order EH action + declared regularization/falloff contracts)", "folded": "No \u2014 gravitational variational calculus, not a trig identity", "notes": "\u2014"},
        {"id": "B22.7", "verdict": "PROVED", "claim": "Conditional channels: (a) gauge \u2014 radial electric charge as cyclic radial momentum p_\u03a6 conjugate to the radial gauge phase (Maxwell dynamics and e imported); (b) rotation \u2014 angular momentum as p_\u03a9 conjugate to frame dragging (imported Kerr channel); (c) spin (Einstein\u2013Cartan) \u2014 axial contorsion exactly auxiliary, torsion solved algebraically for the spin current.",
         "scope": "PROVED-conditional (respective imports: Maxwell, Kerr geometry, Einstein\u2013Cartan)", "folded": "No \u2014 representation of imported physics in canonical coordinates, not trig",
         "notes": "None derives its import (the book's own guard)."},
        {"id": "B22.8", "verdict": "PROVED", "claim": "Kerr/Kerr\u2013Newman half-angle identities: on the imported Kerr geometry the horizon radii satisfy exact half-angle identities in the book's coordinates, extending to Kerr\u2013Newman after the electromagnetic import; guards: valid on the declared regular domain (coordinate singularities excluded), consequences of the imported metric, no new black-hole physics.",
         "scope": "PROVED-conditional (imported Kerr/KN geometry + declared chart domain)", "folded": "No \u2014 conditional coordinate identities; the explicit formula is not stated on the rewrite page, so no trig identity could be verified or folded",
         "notes": "What would close the formula gap: the half-angle identity as stated in the source T6 essay-book or the Kerr-geometry derivation."},
        {"id": "B22.9", "verdict": "PROVED", "claim": "Spherical-spin obstruction (the book's hardest negative): spherical symmetry forces the total spin current to integrate to zero over the sphere, so the canonical spin apparatus cannot be promoted to a theory of spin in the spherical sector.",
         "scope": "PROVED (negative theorem)", "folded": "No \u2014 symmetry argument, not a trig identity",
         "notes": "Proof: a non-zero total spin vector would select a preferred spatial direction, contradicting rotation invariance of the spherically symmetric configuration; hence the integrated spin current vanishes."},
        {"id": "B22.10", "verdict": "ASSERTED", "claim": "Does-not-establish ledger (Dirac equation, spin-\u00bd, \u03b1, Coulomb, EFE, G, Maxwell, e, Kerr metric, EC coupling, masses, couplings, new observables \u2014 none derived); book closure \u0394_op = \u2205, C0 retained; forward boundary (C0 defeated only by a future Class-C model with a measurement contract). The source's Yang\u2013Mills attribution is not repeated (absent from the cited text).",
         "scope": "ASSERTED (the book's own ledger/conclusions)", "folded": "No \u2014 meta, not a trig identity", "notes": "\u2014"},
    ],
}


def main():
    os.makedirs(os.path.join(HERE, "book21"), exist_ok=True)
    os.makedirs(os.path.join(HERE, "book22"), exist_ok=True)
    with open(os.path.join(HERE, "style.css"), "w") as f:
        f.write(CSS)
    with open(os.path.join(HERE, "index.html"), "w") as f:
        f.write(INDEX)
    with open(os.path.join(HERE, "book21", "index.html"), "w") as f:
        f.write(book_page(book21))
    with open(os.path.join(HERE, "book22", "index.html"), "w") as f:
        f.write(book_page(book22))
    print("wrote docs/index.html, docs/book21/index.html, docs/book22/index.html, docs/style.css")


if __name__ == "__main__":
    main()
