# Roadmap item 1: Chapter XII's road law against the evolved distance and redshift work (derivation only; no run)

Sean Brady, 2026-10-23: "word" on the roadmap whose first item is "XII road law against the evolved distance and redshift work". Lead's derivation from the living
text (Chapter XII §2–8, pages 226–229; Chapter IV Part C §47–49 and Appendices E–F, pages 68–107; Chapter III §40–46), the aq_identification campaign report
(ironclad, 2026-10-19), the Volume I repository's PRIOR_WORK.md (sealed core readouts), and the closing-section review of 2026-10-18. Symbolic checks by sympy
(exact). Companion document; nothing in the living text is changed by it. Engineering register. Directed by Sean Brady. Executed with Claude Code.

## 1. The two objects

**Chapter XII's frozen road.** A_los(z) = (1/π)(1 − (1 + z)^{−3}); f(z) = 1 − A_los; in s = ln(1 + z), f(s) = (1 − 1/π) + (1/π)e^{−3s}, with dA/ds = 3(1/π − A).
Small-z coefficients 3/π, −6/π, 10/π (checked). Used as an absolute distance map, D_native = f·D_readout, with the consequences q_0,inferred = q_0 − 6/π (eq. 24)
and, for a luminosity-only map, a duality ratio η_D = 1/f (eq. 22).

**Chapter IV's evolved finite-redshift law.** Ξ(s) = Ξ_∞ + (1 − Ξ_∞)e^{−ps} with (p, Ξ_∞) estimable from data under a declared positive response class, the
compatible amplitude coefficient δ(s) = p(1 − Ξ_∞)e^{−ps}/Ξ(s), the positive-spectrum endpoint bounds (Ξ(s) − E)/(1 − E) ≤ Ξ_∞ ≤ Ξ(s) with E = e^{−p_min s},
finite-window minimax bounds (Appendix F), Fieller sets for the calibration, and the explicit statement that "positivity of this declared action selects neither
a single power nor its exponent". Crucially, Ξ is defined as a ratio of two channels: Ξ(z) = d_L^{GW}/d_L^{EM} = η_GW/η_EM with η_X = d_L^X/[(1 + z)²d_A], and
d ln Ξ/ds = ½ d ln Q/ds for a declared transport coefficient Q.

## 2. What the comparison shows

1. **Same function, one member of the family.** XII's f(s) is exactly IV's Ξ(s) at p = 3 and Ξ_∞ = 1 − 1/π. The general small-z coefficients of 1 − Ξ are
   (1 − Ξ_∞)p, −(1 − Ξ_∞)p(p + 1)/2, (1 − Ξ_∞)p(p + 1)(p + 2)/6; at p = 3 they are (1 − Ξ_∞)·(3, −6, 10), which with 1 − Ξ_∞ = 1/π are XII's three
   coefficients (checked symbolically). XII's p = 3 = d̂ and its plateau are therefore the two selected identifications that pin IV's two free parameters.
2. **The deceleration shift generalises and shrinks.** From D_C/Ξ fitted to the same form, q_0,inferred = q_0 − 2p(1 − Ξ_∞) (derived independently; at p = 3,
   Ξ_∞ = 1 − 1/π it is XII's q_0 − 6/π = q_0 − 1.91). With IV's own fiducial (p, Ξ_∞) = (3, 0.90) the shift is 0.60. XII's "large shift" is the pinned-plateau case.
3. **The objects are not the same observable.** IV's Ξ is a relative amplitude between two carriers reaching one receiver (GW against EM), a ratio in which
   the common geometry cancels: it is tested only by standard sirens, and IV's Appendix F proves its plateau is poorly determined from low-redshift data
   (σ_Ξ∞ ≈ 0.205 low-only, 0.019 with three bands). XII's f is applied to a single channel's distance as an absolute map. XII itself shows (eq. 22) that a
   luminosity-only map gives η_D = 1/f, which at z = 1 is 1.386, a 39 % duality violation; the closing section records that η_D is tested at the few-percent level to
   z ≈ 1.5. A common rescaling of both distances leaves η_D = 1 but moves every other distance comparison (XII §8). So: as an absolute single-channel map the
   frozen road is excluded by distance duality; as a channel ratio it is IV's Ξ with two parameters pinned by selection. The road law survives only in IV's form.
4. **The rapidity reading, flagged as a reading.** The evolved accumulation law (aq_identification; the sealed core's reservoir) has the available fraction
   q = sech²φ = e^{−Λ} with φ the additive rapidity along the path and Λ = 2 log cosh φ. If f were e^{−Λ(s)} the frozen road would say Λ saturates at
   −ln(1 − 1/π) = 0.3832, i.e. the line-of-sight rapidity saturates at atanh(π^{−1/2}) = 0.6390. The core itself keeps the two apart: `gen6.source_clock`
   "receives the original line-of-sight available fraction without identifying it with canonical q". Nothing in the record identifies them, and this note does not.
5. **What XII's "fate" needed and does not have.** Items 2–3 leave H_fit,∞ = H_0Ω_Λ^{3/2} as what XII already calls it, a distance-fit coefficient under a future
   observing family that is not defined; with the absolute map excluded, nothing remains of it to carry.

## 3. Consequence for the placement (for Sean Brady's word; nothing moved)

- Chapter XII §2–8 (road, fate coefficient, finite-redshift tests, duality) should be rebuilt as a short section of Chapter IV Part C: "the p = 3, Ξ_∞ = 1 − 1/π
  member", stating that the plateau and exponent are selected, that the law is the channel ratio Ξ and not an absolute distance map, and that its duality
  consequence as an absolute map is excluded at few percent. The derivation above is the content of that section.
- The title "Cosmological fate" is retired; there is no fate law in the chapter (its own §5–6 say so).
- XII §9–18 (the Home recurrence, custody, the transfer toys) go with the boundary chapter, as the roadmap already proposes.
- One new line for the ideas file: the frozen road's exponent p = 3 is d̂; whether IV's estimable p would come out at d̂ from standard-siren data is a prospective
  test with a declared value, and it is the only place in Chapters VIII–XII where a selected identification could be tested without external data having chosen it.

## 4. What this did not do

No data, no fit, no run. It compared two declared functions and their stated observation maps, derived the general deceleration shift, and read the record's
own words on what identifies with what. Independence: none in CLAUDE.md §8's sense; the symbolic checks are the lead's.
