# Concept note 1 — The static exterior theorem: what the two readings of A(r) give, and where SAM parts from GR

Sean Brady, originator and conceptual director. ChatGPT, Codex and Claude as AI research collaborators; this note AI-assisted writing (Claude Code), 2026-10-29. The theorem was proposed by web Claude in Sean Brady's words of 2026-10-29; the corrections and the framing below are recorded with their authors. Verification: Courtroom II case `voli_metric/01_static_exterior_theorem` (standard-library computation, predictions sealed first).

## In plain language

SAM has three core objects: the floor A₀, the lift A(r) = r_s/r of a source, and the ceiling 1/π of the line of sight. Volume I already declares how a clock and a ruler read the lift: a clock at accumulation a runs at √(1−a) of a far clock (Chapters III–IV, "a declared receiving law"), and r is the areal radius (Chapter V). Add one more declared reading, that the radial ruler stretches by 1/√(1−a), and the three together are Schwarzschild's metric, exactly. Everything a solar-system experiment can see in a static vacuum follows at once: light bending, Mercury's perihelion, the Shapiro delay that Cassini measured, gravitational redshift, the gyroscope precession of Gravity Probe B, all with the general-relativistic values. Cassini's γ − 1 = (2.1 ± 2.3)×10⁻⁵ becomes a measurement of the ruler reading itself.

That does not make SAM general relativity. GR gives Newton's numbers in weak fields and nobody calls GR Newton's work; equal numbers in a regime do not make equal theories. SAM's readings are its own: light runs the road at c_eff = c(1−a), the Shapiro delay is the road operator ∫a dℓ/c, the clock is an interacting source receiving a lapse, not an ideal oscillator in a curved manifold. And the two theories part at the horizon. On this very metric the static coordinate time to A = 1 diverges while the infaller's proper time stays finite. GR reads the divergence as a coordinate artifact and continues through an extension; SAM reads the road as ending at A = 1: the astronaut does not run out of clock, the astronaut runs out of road (Chapter V). That is the one known departure, and the chapter should state it as the postulate it is, with the GR crossing beside it as the comparison.

## The three objects

- **A₀**, the floor: A₀ = 1/(12π) in the convention of Chapters II–III. It drops out of every static exterior observable under the source-only reading N = √(1−a). Under the background-normalized reading √(1 − a/(1−A₀)) the lift's slope is rescaled by 1/(1−A₀) = 1.02725, absorbable only by recalibrating GM consistently in every receiving law. Chapter IV adopts the source-only reading conditionally; the theorem below assumes it and says so.
- **A(r)**, the lift: a = 2GM/(c²r) = r_s/r for an isolated source, the Poisson kernel's exterior solution (Chapter III).
- **The ceiling**: the line-of-sight accumulation saturates at 1/π (Chapter XII, A_los(z) = π⁻¹[1 − (1+z)⁻³]); 1/π = 12 A₀ R with R the count convention. The ceiling plays no part in the static exterior; it is where A₀ and the lift meet the cosmological chapters.

## The theorem

**Static exterior theorem (agreement).** Let a = r_s/r in areal radius, r_s = 2GM/c², 0 ≤ a < 1. Declare three readings: a static clock runs at N = √(1−a); the radial ruler reads dℓ = dr/N; the tangential ruler is areal, so a sphere of radius r has area 4πr². Then the line element is

ds² = −(1−a) c² dt² + dr²/(1−a) + r² dΩ²,

which is Schwarzschild's metric in its own coordinates. Consequently:

1. In the parametrized post-Newtonian expansion γ = β = 1 and every other parameter of the static vacuum sector is zero. Proof by the exact isotropic transformation r = ρ(1 + r_s/4ρ)²: with U = GM/(c²ρ), g₀₀ = 1 − 2U + 2U² − (3/2)U³ + …, g_ij = (1 + 2U + (3/2)U² + …)δ_ij, so 2β = 2 and 2γ = 2, with no remainder at any order (computed as exact rationals in the case).
2. Gravitational redshift to first order: Δν/ν = ΔΦ/c² (the coefficient ½ in a belongs to N).
3. Light deflection at the solar limb (1+γ)/2 × 4GM/(c²R_⊙) = 1.7512″.
4. Shapiro delay, one way: (1+γ)GM/c³ × ln(…) with (1+γ)GM/c³ = 9.851 µs; this is Chapter IV's road operator c⁻¹∫a dℓ at γ = 1. Cassini: γ − 1 = (2.1 ± 2.3)×10⁻⁵ (Bertotti, Iess, Tortora 2003), read here as κ_s − 1.
5. Perihelion advance (2+2γ−β)/3 × 6πGM/(c²a(1−e²)) per orbit: 42.98″ per century for Mercury, the factor equal to 1.
6. Geodetic precession (1+2γ)/3 × (3/2)(GM_⊕)^{3/2}/(c² r^{5/2}): 6606 mas/yr at Gravity Probe B's semimajor axis of 7027.4 km (measured 6601.8 ± 18.3; at mean Earth radius plus 642 km the same formula gives 6638, the number the case's sealed input produced before the orbit was corrected, kept on record).

Controls (computed): γ = ½ gives 1.3134″ and 7.388 µs; β = 2 gives 28.65″ per century. The numbers depend on the readings.

## What the theorem is, and is not

- **It is a conditional theorem under declared readings**, the volume's second register. The ruler reading 1/N is new as an explicit sentence but not as content: Chapter IV already notes that the retained road operator is the γ = 1 case, so κ_t + κ_s = 2 with κ_t = 1 fixes κ_s = 1 at first order from an existing SAM declaration, and Chapter V's exterior logarithmic road (the tortoise coordinate, dr/(1−a)) is the optical road of exactly this metric. The theorem joins three declarations the volume already makes.
- **It closes the open coefficient of Chapter IV by declaration, not by derivation.** The honest sentence is the one Chapter IV already uses for the clock: it is a declared receiving law, and Cassini tests it. A spatial coefficient derived from the retained source action would be the derivation; that remains the interface the closure appendix names.
- **It does not cover frame dragging.** A static zero-shift metric has g_tφ = 0 and no Lense–Thirring term; Gravity Probe B's 37.2 ± 7.2 mas/yr needs a rotating source and a declared shift reading, which is a derivation, not a sentence. Gravitational radiation, preferred-frame effects and the strong equivalence principle for self-gravitating bodies stay on the open list, as the closure appendix has them.
- **It does not say SAM is GR.** It says the static exterior numbers agree. The departure is the horizon road, below.

## The horizon road: same arithmetic, different reading

On the metric, radial light obeys dr/dt = ±c(1−a): the coordinate speed on the road is c_eff = c(1−a), exact, while a local static observer always measures c. The tortoise coordinate r_* = r + r_s ln(r/r_s − 1) diverges at r_s. For infall from rest at infinity the proper time from r to r_s is (2r_s/3c)[(r/r_s)^{3/2} − 1], finite, while the coordinate time over the last thousandth of r_s to the last millionth is 6.9 r_s/c and grows without bound (Chapter V's closed forms, recomputed in the case). These are facts of the metric. GR's reading: the divergence is a coordinate artifact removed by the ingoing extension, and the infaller crosses. SAM's reading: the parent ledger ends at A = 1 and the road ends with it. Chapter V currently carries the GR crossing as the benchmark and the SAM road-ending as a conditional hypothesis; the Chapter I rework can state the road-ending as SAM's declared law with the GR crossing beside it as the control. The decider for the departure, an observable that distinguishes a road ending at A = 1 from an extended interior, is not registered; it belongs to the horizon-scale material of Chapters V and XI.

## For the Chapter I rework

Order of introduction: A₀, A(r), the ceiling; then the two readings of A(r) and the agreement theorem as the first result; then the departure as the first stated postulate; then the SAM readings of light (c_eff, the road operator) with their GR-equal numbers; then the interacting clock, which can move to its own chapter. Chapters IV and V then point to the theorem instead of carrying their own benchmark language, and Appendix A's "decisive join" on κ_s is restated as: declared, tested by Cassini, derivation open.

## Credit

Sean Brady: the three core objects as the introduction; the framing that SAM is not GR and that the departure is the horizon road; the direction to expand concepts before reworking the volume. Web Claude: the metric theorem as item 1, with its list of what it closes. Claude Code: the corrections (frame dragging not closed by a static metric; κ_s closed by declaration, not derivation; the road operator already fixing κ_s = 1 at first order; the GP-B orbit input), the computation and this note.
