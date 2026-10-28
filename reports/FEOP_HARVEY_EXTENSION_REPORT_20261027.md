# FEOP: the Harvey extension program. A report on the state of the work, 27 October 2026

**Attribution:** Sean Brady, originator and conceptual director. OpenAI ChatGPT and Codex (GEN3/GEN4 campaigns) and Claude Code (the October Duck runs and this report) as AI research collaborators, in the project's standing form. AI-assisted writing.
**Prepared by:** Claude (lead), at Sean Brady's request of 27 October 2026 ("produce a detailed report on feop work specifically as it might relate to an extension of Harvey's existing work").
**Register:** engineering. Every statement below is traceable to a record named in the text. BOUND_C02 remains CANDIDATE. Nothing here is a claim of a theorem beyond what the record says, and the one place where this report adds its own derivation is labelled as the lead's.

---

## 0. Summary

FEOP is the program's name for the work that grew out of David Harvey's paper *Faster Enumeration of Primes* (arXiv:2606.22851v1, 22 June 2026). Harvey gives the first algorithms for listing all primes up to N that beat the sieve of Eratosthenes by a positive power of log N, and in two remarks he points at refinements he did not carry out. Remark 6.10 suggests pruning output residue classes that cannot hold square-primes. Remark 8.8 suggests that the local-density constant Δ in his sieve theorem (Theorem 8.7) can be replaced by a smaller Δ′ that sieves higher odd prime-power valuations, not only valuation one.

Sean Brady took both remarks as a research program. It ran in three phases.

1. **The feop_extension repository** (private, GitHub `iwtbotiwtwot/feop_extension`, snapshot commit 319eca0, 89 files). Finite, exact, reproducible implementations of both directions: H01 (Remark 6.10, output-residue pruning) and H02 (Remark 8.8, higher-prime-power local sieve factors), with a one-command replay that passes from a fresh clone. It states what it does not claim: no new headline complexity, no global Δ′ theorem, no full-core speedup.
2. **The GEN4 Harvey series, 1–2 October 2026** (ironclad ledger H002093 to H002143, about thirty entries; campaign folders under SAM_Research_Project/GEN4/harvey_*). The computational campaign behind the repository: 126 source families counted exactly at lengths 10^6 and 10^12 at three starts, a finite Selberg interface with its actual remainder, sparse completion of 1.26 million candidates, and on the H01 side a phase-polynomial compressed stage with a measured 5.9× kernel reduction. Also two side transfers: Harvey's Lemma 8.19 imported into the reciprocal-history (RH) allowances, and Harvey's generating-function identity used for exact prime-event history reconstruction.
3. **The GEN6 Duck FEOP runs, 20–21 October 2026** (ironclad H002737 to H002742, H002759, H002761; nine runs). Peers working on the nested tuple family found that the candidate bound BOUND_C02 is the fixed-cutoff Selberg sieve specialised to the family, computed its exact remainder, found a depth-uniform two-sided bracket, and then found the object that is the real result of the whole program: an exact **4×4 transfer operator** that carries residue-class counts level by level through the p-adic tree, with spectrum {p², 1, p⁻²}, a closed-form finite-depth remainder, and exact multiplicativity across primes. It was verified in the program's verification form (everything given, separate code, predictions written first) at primes and depths never enumerated before.

**Where this stands against Harvey.** Everything established is *local*: fixed prime, fixed tuple family, finite depth, exact. It is precisely the arithmetic Remark 8.8 asks for, and it is complete for the nested family and, by the offset-tree rule, extensible to arbitrary tuples. What is not done is the *global* step: inserting a Δ′ with a uniform remainder into Theorem 8.7's error term, in Harvey's normalisation (common slope U, offsets 0 ≤ u_i < U, Q(u) the product of the bad primes), averaged over tuples as Section 8.5 requires, with the growing-g uniformity Sections 9–10 need. The record says this plainly in every run report, and so does this one.

**The lead's assessment of the nearest honest extension.** The transfer operator gives, for the first time in this program, an exact and cheap handle on the one quantity that controls Remark 8.8's insertion: the finite-depth truncation error at each prime, N·R = g/(p+1) from depth g−1, which is g/((p+1)p^{2L}) in density. That number is what decides how deep one must sieve at each prime before the tail is negligible against the main term. A depth schedule L_p that keeps the product of moduli within the sieve's level of distribution while the summed tail stays below the main-term gain is a concrete, finite-dimensional lemma that nobody has written yet. Section 6 sets it out. It is the step that would turn "we computed Δ′ locally" into "Remark 8.8 holds for this family with this constant". It is also small enough to be written, checked by independent code, and shown to Harvey.

---

## 1. Harvey's paper and the two openings

**The result.** Harvey's main algorithms enumerate all primes up to N in N(log log N)^{1+o(1)} bit operations (heuristic variant), with rigorous randomised and deterministic variants slower by (log log N)^{1+o(1)} and (log N)^{1/2+o(1)}. The engine is a generating function over F₂ for *square-primes* (integers m²p with m odd and p an odd prime), fast polynomial arithmetic, and a compression step borrowed from error-correcting codes that recovers a sparse set of exponents from power sums.

**Remark 6.10 (p. 51).** Square-prime exponents are restricted modulo squares of small primes: m²p is never 10 or 15 mod 25, and 5 or 20 mod 25 only when p = 5. Harvey says a suitable wheel W and some reorganisation might improve one term by φ(W)/W, a possible log log log N speedup of the heuristic variant. "The author has not checked the details."

**Theorem 8.7 (p. 77) and Remark 8.8 (p. 78).** The sieve theorem counts k ∈ [0, X) such that Uk + u₁, …, Uk + u_g are all square-z-rough. It sieves residue classes B_p = {k mod p² : p | Uk + u_i, p² ∤ Uk + u_i} (Lemma 8.4) and gets a bound g!ΔX/(log z)^g (1 + O(θ/log z)) + O(z²(log z)^{4g}/(2g)!²), with Δ = ∏_p (1 − |B_p|/p²)(1 − 1/p)^{−g} (equation 8.4). A prime is *bad* if p | U, or p divides some u_i − u_j, or p ≤ 4g²; Q(u) is the product of the bad primes. For good primes |B_p| = g(p−1) (Lemma 8.6). Remark 8.8: Δ can likely be replaced by a smaller Δ′ that also sieves {x ≡ 0 mod p³, x ≢ 0 mod p⁴} and so on, by analogy with the squarefree density ∏(1 + p⁻² + p⁻⁴ + …)⁻¹ ≈ 0.6079 against ∏(1 + p⁻²)⁻¹ ≈ 0.6580. "The author has not checked the details."

**Why it matters to Harvey's algorithm.** Theorem 8.2 (p. 76), proved from 8.7 by summing over all tuples u ∈ {0, …, U−1}^g (Section 8.5), bounds how many intervals of length U carry at least g square-y-rough integers. Section 9.4 names the removal of the factorial loss at order g ≈ log log N as the consequential route to a better exponent. A smaller Δ′ improves a constant inside this chain; whether it changes the exponent depends on the factorial-moment estimate, which Harvey's Lemma 8.19 (the divisor-sum bound (log z)^g/g! ≤ Σ τ_g(n)/n ≤ (log z + g)^g/g!) controls.

**The name.** FEOP is the acronym of the paper's title. In the record it names the program, not the paper.

---

## 2. The feop_extension repository (snapshot 319eca0)

The repository is private; no clone exists on this machine and the GitHub API returns 404 to the public. Its full tree at commit 319eca0 is retained byte for byte, with SHA-256 custody, in the abandoned Codex campaign `retained/codex_abandoned_20261020/campaigns/feop_h02_growth_20261020/sources/feop_extension/` (89 files, 3,872,950 bytes). Whether the GitHub repository has moved past 319eca0 could not be checked; this report describes the snapshot.

**Scope and attribution as the repository states them.** Harvey's framework, square-prime formulation, restricted products, compression scheme, square-rough sieve and the two remarks are Harvey's. The repository adds finite implementations and derivations. Its CITATION.cff lists Sean Brady, OpenAI ChatGPT and OpenAI Codex as authors; by Sean Brady's decision of 27 October 2026 (decisions log) the author is Sean Brady and the two tools are instruments. Harvey is cited, not redistributed, and not listed as a contributor. A proposed email to Harvey exists in `notes/PROPOSED_EMAIL.md`; it was never sent. No licence is granted.

**H01, output-residue pruning (Remark 6.10).** Over F₂ with a wheel W = ∏p² of distinct odd primes, a depth-L mask rejects an exponent whose p-adic valuation is odd and below 2L. Discarded desired terms always have a distinguished prime in the wheel, and the exception series E_exc = Σ_p [F(x^p) + F(x^{p^{2L+1}})] with F(x) = Σ_{m odd} x^{m²} restores them exactly, so A = mask(A) + E_exc. The prime-power correction E1 and the restricted-product boundary E2 are kept. Headline fixture at N = 7200, M = 900, W = 225: regular slice products 4,317 → 3,333, coefficient products 4,383 → 3,380, 31 exceptions restored, every output coefficient equal to the unmasked reference, 12 saved configurations and 21,528 coefficients replayed. A later bounded compressed stage (N = 3528, M = 882, W = 441, GF(1024)) ran 1.197× faster masked, with field multiplies 1,213,464 → 1,000,308, but all 56 blocks fell back to exact reconstruction, so no useful sparse decoding was shown. Open: integrating the mask into an efficient transform backend, a compression regime with real block sparsity, and locating the gain inside Harvey's cost formula.

**H02, higher-prime-power local sieve factors (Remark 8.8).** The local engine takes a prime p, a positive slope U and integer offsets, normalises U = p^a V, resolves fixed valuations, and walks a grouped root tree; an isolated root at depth d closes exactly with conditional acceptance p/(p+1) or 1/(p+1) by parity, so the infinite-depth local factor is exact without enumerating a period. The separated-root tail is τ_p = q/((p+1)p^{N−a}) with q compatible roots. An interval evaluator counts a half-open interval exactly from signed residue cylinders with no floating point, and separates accepted (S), resolved (R), unresolved (Z), boundary discrepancy (E) and the all-depth count (T). Sparse completion subtracts future rejections over an exhaustive cover of unresolved cylinders. A finite Selberg interface (z = 5 or 7 only, by design) carries exact weights, the full Gram matrix and the signed remainder, and groups terms of equal LCM before taking absolute values: tighter in 60 of 72 non-obstructed cases, equal in 12. A full sparse Gram update retains already-rejected positions (16 of 24 controls have a nonzero contribution from them). Results: 126 selected families complete at 10^6 and 10^12 at starts 1, 10^20+7, 10^60+17; 452 of 504 family/horizon combinations complete; family 24 (U = 1024, offsets 0..3, primes 3, 5, 7, 11, L = 7) completed from 418,811 candidates per interval with 11,624 future rejections, all-depth counts 18,518,518,579 / 497 / 594.

**What it does not claim**, in its own words: the global Δ′ theorem, the growing-g uniform estimate, the factorial-loss removal, an end-to-end H01 speedup, and a literature-wide novelty claim for CRT, sparse updates, LCM grouping or classical Selberg identities. Its OPEN_PROBLEMS.md gives five success conditions per track; the five H02 items are the honest map of what an extension of Harvey still needs.

---

## 3. The GEN4 Harvey series, 1–2 October 2026

The repository is the distillation of a two-day computational campaign recorded in about thirty ledger entries. The chain, in order, with the number that each step added:

| Entry | Campaign | What it established |
|---|---|---|
| H002093 | prime_harvey1 | Reading of the paper for the prime-event work; Harvey's equation 2.7 checked on 4,097 coefficients; exact rank-transport reconstruction of a prime-event history from a reference plus sparse discrepancies |
| H002094 | rh_harvey_companion1 | Harvey's Lemma 8.19 polynomial P_g(L) = Σ C(g,j) L^j/j! imported into the RH paid allowances: (F−1)P₄(2 log K) and 2J(F−1)P₈(2 log K); factors 12.36 and 2833.8 at K = 1024; an exact RH consumer with 4.1× less tracked allocation |
| H002095, H002097 | prime_harvey2, 4 | Exact raw-history reconstruction of 55,662,472 prime events; stretch correction 3.5–30% faster |
| H002105 | harvey_h02_extension1 | The general local-factor engine: 616 cases, 5,668 checks, 1,099,168 enumerated residues; the tail formula q/((p+1)p^{N−a}) |
| H002106 | harvey_interval_bridge1 | The exact interval bridge S = Hδ + E with its remainder account; a 101^64-period case counted at length 10^80 from 89 terms |
| H002107–H002125 | interval budget, query, retry, CRT structure, streamed CRT, depth selection, pair/triple/four-prime calibrations | The 672-candidate roster completed; prepared queries 26–458× faster; group-streamed CRT with working groups ≤ 280 terms; depth tables for 126 families |
| H002127 | harvey_integer_synthesis1 | Common-period integer accumulation 1.65×; the local-root cover certificate Z ≤ B_root (1,347 of 1,350 zero-unresolved cases certified); the sparse-completion method derived |
| H002128, H002129 | sparse completion, family 24 | Family 23 and family 24 completed exactly (the 1,256,434 candidate records) |
| H002132 | harvey_h02_h01_interface1 | The 96-case finite Selberg interface (72 nontrivial, 24 obstructions); H01's 12 legal configurations and 31 exceptions |
| H002136 | harvey_grouped_core1 | Grouped-LCM remainder (60 strict improvements); full sparse Gram update with already-rejected positions; the bounded compressed stage 1.197× |
| H002138, H002140 | remainder_grouping2, phase_compatibility3 | Start-uniform remainder envelopes by exact circular-window extrema per modulus (72 cases tighten); H01 phase-polynomial transforms 5.92× on the kernel |
| H002142 | harvey_scale_budget4 | H01 at N = 14,112 / 28,224: phase speedups 4.66× / 1.39× unmasked; the offsets-30j family is exactly obstructed at p = 7 for all g ≥ 14 |
| H002143 | harvey_hybrid_nested5 | The **nested family** A_g = {0, Q², …, Q^{2(g−1)}}, Q = 2310, with selected-prime density ≥ 16/77 at every g and depth; budget hierarchy with lift work ≤ S₀ + B; "the retained next question is a recurrence coupling g and L" |

Three things to note about this phase. First, the nested family was chosen because the earlier 30j family dies at p = 7; it is a family built to survive the selected primes, and every later FEOP result is about it. Second, the two side transfers go the other way: Harvey's lemma improved RH's constants, and Harvey's identity gave prime-event history compression. Neither is an extension of Harvey; both are uses of him, and the RH companion report says so ("not an implementation of Harvey's sparse inverse-transform algorithm"). Third, every entry in the series closes with the same boundary: "Global H02 / growing-g / full H01 consumer remain OPEN."

---

## 4. The Duck FEOP runs, 20–21 October 2026

The Duck is the program's peer-run instrument: four research peers on a fixed window, a lead outside, exact native receipts for every identity, declared controls that must fail. Nine runs touched FEOP. Their records are the ironclad entries, campaign folders and doc-repo run records named below.

| Date | Run | Entry | Returns | What it did |
|---|---|---|---|---|
| 20 Oct (night of 19th) | feop_h02_growth (Codex, abandoned branch) | triaged in `sandbox/abandoned_codex_20261020/TRIAGE.md` | 281 | Produced the six CANDIDATE records: LOCAL_R1 (density recurrence), LOCAL_R2 (signed-cylinder count T = m(2L−m+1)), CRT_EVEN_SEPARATION_CYLINDERS, BOUND_C01, BOUND_C02, CONTROL (fixed-prime floor). The lead's triage: C01/C02 read as the Selberg upper-bound sieve specialised to the family; literature unchecked |
| 20 Oct | feop_bound_c02 (run 1) | H002737 | 74 | Three peers converge: at fixed z the sieve is a finite CRT product; Legendre's two-sided identity executed natively (16,807 cylinders, starts to 10^15); Selberg with the full roster has the Legendre normaliser exactly; C02's roster d ≤ z leaves its main term a constant above the true density (0.3496 vs 0.2879 at z = 7). Closed form D_g(L) found by two peers separately. The **depth-uniform two-sided bracket** appears (BOUND): 6.5× below C02 at X = 4^16 |
| 20 Oct | feop_bound_c02_rerun (blind, worktree at pre-run commit) | H002739 | 61 | First tier recurs by different constructions. New: the **exact Selberg remainder** B_z(g) = Σ|γ_m|T^{ω(m)} with leading constant 1.44 (z = 7) and 3.27 (z = 11) against C02's coarse 324 and 576; the C02-frame bound is nontrivial from g = 12 instead of 17 and beats Legendre through g = 19/25; the roster is a free parameter |
| 20 Oct | feop_bound_c02_run3 (installed 2.0.1) | H002740 | 61 | Exact remainder reproduced to four digits by different peers; CRT's additive-discrepancy idea refuted on 22 of 22 rows; the bracket and tree formula remain single-run leads |
| 20 Oct | feop_sidebyside | H002741 | 210 | Bracket steps (a), (b) made native with hypotheses located (nested offsets, p | Q, k ≤ g, k ≤ L); every γ_m sign gated (693 checks); at equal X and z the bracket upper is tightest from g = 2, nontrivial from g = 4/5 against 12/13 (exact Selberg), 17/18 (C02), 17/23 (Legendre); sharpened step (b′) narrows the width 20–25% |
| 20 Oct | feop_bracket_fiber | H002742 | 298 | Fibering past the 64-row word limit: receipts to p = 11, 1.77 million residues; the obstruction is the residue count p^{2k}, not the matrix limit; the open idea: a receipt per cylinder level, a transfer operator |
| 21 Oct | rh_crossover_1 | (RH-side run) | 315 | The local remainder shrinks exactly p⁻² per level from depth g−1; N·R = g/(p+1); the Selberg remainder's leading constant is one ω-level's |γ| mass; the same double-root/simple-root split appears in the spin staircases, called a coincidence until one construction unifies them |
| 21 Oct | feop_transfer_1 | H002759 | 447 | **The transfer operator**: four classes (settled S, dead X, zero Z, tracking T), two exact 4×4 matrices A (split level) and B (no split), spectrum {p², 1, p⁻²} with a Jordan block at the split, iterate to level 24 equals the closed form, Kronecker multiplicativity across primes, joint recurrence with roots ∏_{p∈S} p⁻² |
| 21 Oct | feop_verify_1 | H002761 | 346 | Verification form: A and B re-derived four times (twice before reading); counts at p = 11, 13 (L = 2), p = 5 (L = 4, 390,625 residues), p = 3 (L = 5), p = 2 (L = 7, 8) all equal to predictions written first; remainder law at p = 13, 17, 19, 23; joint recurrence with 11 and 13; the hypotheses mapped by break attempts; two wordings corrected |

Design lessons the runs produced are in the ideas log (T10): blind replication in a worktree, the lead's capture kept outside what peers read, declared expected failures (Duck 2.3.3), the fibering library with partition receipts in place of an engine release.

---

## 5. What is in hand, stated exactly

All of the following concern the nested family A_g = {0, Q², …, Q^{2(g−1)}}, Q = ∏_{p≤z} p (so p | Q with v_p(Q) = e = 1 for the selected primes), the predicate "n is rejected at p when v_p(n + o) is odd and ≤ 2L − 1 for some offset o", and the counts over residues mod p^{2L}. Receipts are native unless stated.

**5.1 The local density, closed form.** D_g(L) = 1 − (p−1) Σ_{h=1}^{L} min(g, h) p^{−2h}; certified on 64 rows; limit D_g(∞). The number of offsets split off by level h is min(g, h) because offset o_j (valuation 2j at p) leaves the zero class at level h = j. Single offset: D_1(∞) = p/(p+1), which equals the good-prime higher-power factor (Section 6), as it must.

**5.2 The finite-depth remainder.** R(L) = D_g(L) − D_g(∞) = (p−1) Σ_{h>L} min(g,h) p^{−2h}. From L ≥ g−1 this is exactly g p^{−2L}/(p+1), so with N = p^{2L}: **N·R = g/(p+1)** (recorded; the lead re-derived it from the closed form for this report: for p = 3, g = 3 the sequence (p+1)N R is 19/9, 3, 3, 3 at L = 1..4; for p = 5, g = 4 it is 1276/625, 76/25, 4, 4, 4). One note: the record states the last departure at L = g−2 as −(p−1)/p²; from the closed form the lead reads −(p²−1)/p² (−8/9 at p = 3 against the record's −2/9). The receipts exist; one normalisation is being quoted differently and should be reconciled before either number is published.

**5.3 The transfer operator.** At level h every residue is in exactly one of S (settled, can never die), X (dead), Z (≡ 0 mod p^{2h}, carries o₀ and every unsplit offset) or T (≡ −o_j for one split-off offset). Lifting to the p² children sends (S, X, Z, T) through, with q = p⁻²:

A (split level) = [[1, 0, (p²−2p)q, (p²−p)q], [0, 1, 2(p−1)q, (p−1)q], [0, 0, q, 0], [0, 0, q, q]]
B (no split) = [[1, 0, (p²−p)q, (p²−p)q], [0, 1, (p−1)q, (p−1)q], [0, 0, q, 0], [0, 0, 0, q]]

Start (0, 0, 1, 0); apply A at h = j·e for 1 ≤ j ≤ g−1, B elsewhere. Spectrum: (B−I)(B−qI) = 0; (A−I)(A−qI)² = 0 with (A−I)(A−qI) ≠ 0 (a Jordan block at q). ONE's stationary (g+2)-form with minimal polynomial x^g(x−1)(x−p²) is carried onto the 4-state form by an explicit map Φ (80 zero entries). The iterate to level 24 reproduces D_g(L) at p ≤ 13, g ≤ 24: the bracket's constants at k = 24 come from a 26×26 iterate instead of p^{48} cells. Children at a split: Z has p² children of which 2(p−1) die, one stays Z, one becomes T, p² − 2p settle (corrected wording).

**5.4 Across primes.** Under CRT the joint class state is the tensor product and the joint step is the Kronecker product of the local steps; checked by direct joint enumeration mod (3·5·11)², 5⁴·7², 3⁴·11², 3⁴·5², 3⁶·5², all equal. The joint remainder ∏_p D_p(L) − ∏_p D_p(∞) = Σ_{S≠∅} ∏_{p∈S} (g/(p+1)) p^{−2L} ∏_{p∉S} D_p(∞) for L ≥ g−1, a recurrence with roots ∏_{p∈S} p⁻² (order 2^m − 1); checked with four and five primes. The additive (dead-at-either) prediction misses by the product of dead counts at two primes and by the inclusion–exclusion remainder at three (corrected).

**5.5 Hypotheses, mapped.** The operator fails exactly where two offsets share a class, where a cluster dies whole (odd internal separation), where p ∤ Q, or where the schedule is not set offset by offset by valuation. The offset-tree rule (new-dead classes at level h are the live offset clusters mod p^{2h−1}; a cluster with two or more sub-clusters mod p^{2h} dies whole) matched all ten off-hypothesis tuples tried and is, by one peer's derivation, the exact cluster count for any tuple. It has not been written as an operator.

**5.6 The bound BOUND_C02 and what it is.** S(A, X) ≤ X/H_* + X M_z(g + 4/3)4^{−g} + C_z[g(g+1)]³ with C₇ = 324, C₁₁ = 576, along g = L = ⌈log₄ X⌉ giving X/H_* + O_z(log⁶ X). Three runs agree it is the Selberg Λ² upper-bound sieve (Halberstam–Richert form) on the divisor roster d ≤ z with |r_m| ≤ T^{ω(m)}, T = g(g+1), and the only family-specific inputs are T and the exact normaliser tail. Its main term is a constant factor above the elementary count because the roster truncates (full roster = Legendre, normaliser exactly 1/∏d_p). With the exact remainder (polynomials 4T³+19T²+12T+1 at z = 7, 14T³+34T²+15T+1 at z = 11) it is nontrivial from g = 12/13 and sharper than Legendre through g = 19/25. The literature check is still owed: no external text was in the retrieval index, so "Halberstam–Richert" is the peers' reading.

**5.7 The bracket.** For every k ≤ g: X∏_p d_p(k) − ((1+k(k+1))^{π(z)} − 1) − Σ_p k(Xp^{−2k} + 1) ≤ S_g ≤ X∏_p d_p(k) + (1+k(k+1))^{π(z)} − 1, uniform in g, L and A, so the tuple's diameter drops out. Its two steps (depth-g survivors ⊆ depth-k survivors with D_g(k) = D_k(k); deep deaths in ≤ k classes mod p^{2k}, sharpened to min(g, k+1) classes mod p^{2k+1}) hold natively to p = 11 and k = 2..6 by fibering, break off-hypothesis as they should, and the measured extremes over all starts lie inside wherever a full period was scanned. Reading: S = X∏d_p(∞) + O_z((log X)^{2π(z)}), two-sided. Not a proof; "verified where the program allows, hypotheses located".

**5.8 The obstruction that every run restates.** The largest offset is Q^{2(g−1)}, about X^{11.17} along the logarithmic path. S counts *starts*; it says nothing about whether n + Q^{2(g−1)} lies in any enumeration window. If the tuple must fit the window, g ≤ 4 is forced and every bound is trivial there. The nested family is built for the local theory, not for Harvey's Theorem 8.2, which sums over tuples inside one interval of length U.

---

## 6. How this relates to an extension of Harvey's work

This section separates what the record supports from what the lead reads into it. The reading is marked.

**6.1 What Remark 8.8 asks, precisely.** Replace B_p = {k mod p² : v_p(Uk + u_i) = 1 for some i} by the higher-power set B′_p = {k : v_p(Uk + u_i) odd for some i}, and Δ by Δ′ = ∏_p (1 − |B′_p|)(1 − 1/p)^{−g} with |B′_p| now a p-adic density. Then prove Theorem 8.7 with Δ′ in place of Δ. The second part is where the work is: Theorem 8.7's proof sieves with squarefree d and a level of distribution tied to z; sieving mod p^{2L} multiplies the moduli, so the remainder must be re-controlled.

**6.2 The good-prime factor is elementary (lead's derivation, not in the record).** At a good prime (p ∤ U, p ∤ u_i − u_j, p > 4g²) each offset contributes rejection density Σ_{j odd} (p−1)/p^{j+1} = (p−1)/(p²−1) = 1/(p+1), and the g offsets are disjoint mod p, so

  1 − |B′_p| = 1 − g/(p+1)  against Harvey's  1 − g(p−1)/p².

Checked numerically (p = 13, g = 3: 0.785714 against 0.786982; p = 101, g = 3: 0.970588 against 0.970591). The normalised product ∏_{p good} (1 − g/(p+1))(1−1/p)^{−g} converges (partial products to 20,000: 1.0167, 0.9939, 0.9881 at g = 2, 4, 8). So for good primes Δ′ is a closed form and converges absolutely by the same argument as Harvey's Corollary 8.25. This is the analogue of Harvey's squarefree-density analogy made exact, and it is not in the feop_extension repository or any run; it took one line once the FEOP single-offset factor p/(p+1) was in hand. It should be checked by someone other than the lead.

**6.3 The bad-prime factor is the FEOP result.** Harvey handles bad primes (p | U, p | u_i − u_j, or p ≤ 4g²) by collecting them into Q(u) and accepting a θ = g² log 5Q log log 5Q loss in the error term; for them |B_p| can be anything below p². The FEOP nested family is *all* bad primes with deep collisions (u_i − u_j divisible by Q²), and the transfer operator computes the higher-power local factor there exactly, at every finite depth, with the remainder in closed form. The offset-tree rule extends it to arbitrary tuples. So the two pieces of Δ′ are now both in hand: good primes by the one-line formula, bad primes by the operator. **The record supports the local factor; it does not support any statement about Theorem 8.7's remainder.**

**6.4 The depth-schedule lemma (lead's proposal; the nearest honest extension).** The transfer operator gives the truncation error at prime p and depth L as exactly g/((p+1)p^{2L}) in density for L ≥ g−1 (nested family) and, for a good prime, Σ_{j ≥ L} (p−1)/p^{2j+2} per offset, i.e. g/((p+1)p^{2L}) again. Both are tiny for all but the smallest primes at L = 1. That means a Δ′ sieve does not need depth at most primes. A depth schedule L_p with L_p = 1 for p > p₀ and L_p chosen so that Σ_p g/((p+1)p^{2L_p}) is below the gain Δ − Δ′ keeps the sieve moduli ∏ p^{2L_p} within a bounded factor of ∏ p² and so within the level of distribution Harvey's proof already tolerates. Writing this as a lemma, with the remainder for depth-L_p sieving carried through Harvey's own Section 8 machinery (his Lemma 8.19 bounds the divisor sums), is the concrete step that would make Remark 8.8 a theorem for the nested family and, with the offset-tree operator, for any fixed tuple. It is finite-dimensional, every input is exact, and it is small enough to send to Harvey with the two 4×4 matrices and the plateau identity as its evidence. It has not been attempted.

**6.5 What would still not follow.** Theorem 8.2 averages over all tuples u ∈ {0, …, U−1}^g (Section 8.5) and the algorithmic use needs g growing like log log N (Section 9.4), so three more things stand between a Δ′ for fixed tuples and an improved Harvey algorithm: uniformity of the remainder in g (the (2g)!² term), the averaged factorial moment that Lemma 8.19 feeds, and the normalisation (0 ≤ u_i < U; Q(u) the bad-prime product rather than the fixed 2310). Each FEOP run report says this; the obstacles document of the abandoned Codex run (`feop_obstacles_20261020/OBSTACLE_TARGETS.md`) lays them out role by role. The record is consistent that none of these has been touched.

**6.6 Remark 6.10 (H01).** The exception identity A = mask(A) + E_exc is exact and qualified at depths 1–3; the kernel reduction is real (about 23% of slice products at W = 225; 5.9× on the phase-polynomial stage) but confined to the kernel. Harvey's remark locates the possible gain in the heuristic variant's (6.33) term by φ(W)/W; the record has not placed the kernel saving into that term with its parameter dependencies, and the compressed stage has shown no sparse-decoding coverage (all blocks fall back). An extension here is an engineering result, not a theorem: a matched transform backend with the mask integrated and the cost accounted in Harvey's model.

**6.7 The RH companion is a transfer in the other direction.** Harvey's Lemma 8.19 polynomial replaced a cruder divisor majorant in the reciprocal-history allowances, changing constants only. It is a use of Harvey's lemma, properly attributed, with no bearing on an extension of his paper. The prime-event history reconstruction likewise uses his generating-function identity (equation 2.7) as a tool.

**6.8 Independence, stated plainly.** Every mathematical statement in Sections 3–5 was derived and checked by AI instruments under Sean Brady's direction, and the Duck runs' "independence: none" lines say so in every report. Separate code and predictions-first inside the verification run are real strengths; they are not the independent human review that a note to Harvey would receive. The repository's one-command replay (13 seconds from a fresh clone) is the right artefact for that review.

---

## 7. Status against the volumes and SAMA

- FEOP has no home in Volumes I–III. Volume III Chapter XXII carries one received-results subsection (body10.tex, citing H002759 and H002761) and the engine Part 2 mentions the runs as method examples. The ideas log (T7, T8) records it as a program thread "with no volume home yet", and Sean Brady's note of 22 October places the FEOP operator and bound in a future Volume IV (Reciprocal History) as its own part, with the spin/RH connection recorded as a transfer ledger, not a claimed unity.
- The public SAMA repository holds nothing of FEOP: no run after 29 August, no vol_iv material on sieves. The gap ledger of this morning (SAMA `maintenance/VOLUME_REFERENCE_GAPS_20261027.md`) lists feop_transfer_1 and feop_verify_1 in Tier 1.
- Publishable now without touching the engine: the two 4×4 matrices, the closed form, the plateau identity, the joint recurrence, the hypotheses map, the exact Selberg remainder constants, the bracket statement with its receipts' reach, and the host enumerators (plain Python). Withheld with the construction: the recipe library, the fibered-word library internals, the controller plans. Harvey's PDF is retained locally under `feop_obstacles_20261020/sources/literature/` and must not be redistributed; the repository's own omissions note already says so.

---

## 8. Recommendations, in order

1. **Reconcile the one discrepancy** in Section 5.2 (the last-departure constant) from the receipts before any number is written for an outside reader.
2. **Write the Δ′ local-factor note**: the good-prime formula 1 − g/(p+1) (Section 6.2, to be checked by independent code), the bad-prime factor from the transfer operator, and the convergence of the normalised product. Two pages, every number replayable.
3. **Attempt the depth-schedule lemma** (Section 6.4) on the nested family with Harvey's Section 8 machinery, as a Duck run in the verification form followed by a human-readable derivation. This is the step that turns the local theory into a statement about Theorem 8.7.
4. **Write the offset-tree rule as an operator** on cluster states (ideas log, feop_verify_1, FOUR), so the local factor is available for arbitrary tuples: Harvey's Section 8.5 average needs all tuples, not one family.
5. **Get Halberstam–Richert into the retrieval index** before any write-up names the Selberg comparison (open since run 1).
6. **Decide the outside contact.** The never-sent email in the repository offered Harvey the finite H01/H02 package. The stronger offer now is Remark 8.8 made exact for one family: the two matrices, the plateau identity, and the depth-schedule lemma if item 3 succeeds. That is a result a number theorist can check in an afternoon, with Sean Brady as its author.
7. **Leave BOUND_C02 as CANDIDATE** until item 5 is done and the bracket's steps have a written proof, not only receipts.

---

## Sources

ironclad: `SAM_HISTORY/entries/H002093…H002143` (Harvey series), `H002737…H002742, H002759, H002761` (FEOP runs); `campaigns/feop_bound_c02_20261020/` (TARGET, RUN_REPORT, rerun/, run3/, prior/MATH_REVIEW.md, prior/CANDIDATES.json), `feop_sidebyside_20261020/`, `feop_bracket_fiber_20261020/`, `feop_transfer_20261021/` (prior/LEAD_FRAMING.md), `feop_verify_1_20261021/` (prior/DEFINITIONS.md, prior/VALUES.md), `rh_crossover_20261020/`; `sandbox/abandoned_codex_20261020/TRIAGE.md`.
SAM_Research_Overflow/retained: `codex_abandoned_20261020/campaigns/feop_h02_growth_20261020/sources/feop_extension/` (the repository snapshot 319eca0: README, OPEN_PROBLEMS, HARVEY_PAPER_MAP, CLAIMS_AND_EVIDENCE, SCOPE_AND_ATTRIBUTION, h01/h02 derivations and results, notes/), `feop_obstacles_20261020/` (TARGET, OBSTACLE_TARGETS, sources/literature/Harvey_2606.22851v1.txt).
SAM_Research_Project: `GEN4/harvey_*`, `GEN4/prime_harvey1–4`, `GEN4/rh_harvey_companion1/{REPORT,DERIVATIONS}.md`, `SAM_LIVE/02_RH_CURRENT.md`.
Substrate_Accumulation_Model: `runs/20261020_feop_*`, `runs/20261021_feop_*`, `ideas/IDEAS.md` (T7–T10 and the dated FEOP entries), `decisions/DECISIONS.md`, `volumes/III/src/book_20261025/body10.tex`.
Harvey: arXiv:2606.22851v1, Abstract; Remark 6.10 (p. 51); Section 8.1, Lemmas 8.4, 8.6, equation 8.4, Theorem 8.7, Remarks 8.8–8.9 (pp. 76–78); Lemma 8.19 (p. 82); Theorem 8.2 (p. 76).
