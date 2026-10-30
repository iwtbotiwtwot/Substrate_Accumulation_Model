# Concept note 2 — The clock and the road: two numbers between endpoints, and the SAM law

Sean Brady, originator and conceptual director. ChatGPT, Codex and Claude as AI research collaborators; this note AI-assisted writing (Claude Code), 2026-10-29. The magic bell, its result and the SAM law are Sean Brady's, recorded in his words in `00_STATEMENTS_20261029.md`. Verification: Courtroom II case `voli_clock_road/01_two_numbers`.

## In plain language

Between two endpoints SAM keeps two numbers where most frameworks keep one. The first is the measurable distance of the route, what a ruler laid along it reads. The second is the accumulation looked through along it, how much displaced space the route passes. The magic bell is the picture that keeps them apart. The bell rings with the far clock's strikes and carries nothing else, so it reads the clock, which depends only on the value of A at the two endpoints. The telescope shows the strikes after the light has run the road, so it reads the accumulation. The question the bell asks, whether ring and image arrive in unison, is left unanswered on purpose. What came out of the experiment is better served as an idea than an answer: **if A is not equal at two endpoints, accumulation must exist between them.**

That idea is a theorem in the volume's terms, and it has a twin that is just as important: the converse fails. Two endpoints can have the same A with a great deal of accumulation between them. The Cassini conjunction is exactly that. Earth and Cassini sit at nearly the same A, their clocks agree to one part in a hundred million, and the signal between them looks through thirteen Schwarzschild radii of accumulation and arrives 131 microseconds late. The clock reads the endpoints; the road reads the path; unequal endpoints force a road, but a road does not force unequal endpoints.

GPS is the everyday instance and the question that started the thought experiment: how can accumulation be reconciled with the need to adjust the clocks in GPS satellites? The system makes two separate corrections. The satellite clock runs fast by about 38.5 microseconds a day because of where it sits, the endpoint correction. The signal's road is corrected for its travel, and the gravitational part of that correction is tens of picoseconds per signal. Both come from the one displacement a and are applied separately. Hence the clock and the road.

Read outward along a line of sight, the same idea is the SAM law: **the farther you look out into space, the more accumulation you are looking through.** It is not a challenge to Hubble's law. It offers a different explanation of the same phenomena.

## The two numbers

For endpoints 1 and 2 joined by a route Γ on the static exterior of a source, with a = r_s/r:

- measurable distance: L = ∫_Γ dℓ;
- accumulation looked through: Σ = ∫_Γ a dℓ.

The clock comparison is N(a₂)/N(a₁) = √((1−a₂)/(1−a₁)), a function of the endpoint values alone. The road's delay is (1+γ)Σ/(2c) with γ = 1 by the static exterior theorem (concept note 1), so the delay is Σ/c; its deflection and its reddening of the carrier are likewise functionals of the route. Chapter IV's finite-endpoint logarithm gives Σ in closed form for a straight route: Σ = r_s ln[(r_A + r_B + L)/(r_A + r_B − L)].

**Result (Sean Brady).** a₁ ≠ a₂ ⇒ Σ > 0. Proof: a is continuous and strictly positive along any route; a route joining points with different a has positive length; the integral of a positive continuous function over positive length is positive. Checked on three routes in the case.

**The converse fails.** a₁ = a₂ does not imply Σ = 0. Earth at 1 AU and Cassini at 8.43 AU with impact 1.6 R_⊙: a differ by a factor 8.4 of themselves but both are of order 10⁻⁸, the clock ratio differs from 1 by 8.7×10⁻⁹, while Σ = 13.32 r_s = 39.3 km and the one-way excess is 131.2 µs (round trip 262.4 µs). The far-endpoint approximation ln(4r_Ar_B/b²) agrees with the exact logarithm to 1.4×10⁻⁵.

**GPS.** At 26 560 km: gravitational clock correction +45.7 µs per day, velocity −7.2, net +38.5 (the operational figure is 38.6). The gravitational road term along a zenith route is 42 ps, along a horizon route 62 ps. One displacement, two corrections, kept apart.

## The SAM law along a line of sight

Chapter XII's road law is A_los(z) = π⁻¹[1 − (1+z)⁻³]: zero at the observer, initial slope 3/π, monotone, with the exact limit 1/π, the ceiling. Values: 0.0794 at z = 0.1, 0.2240 at 0.5, 0.2785 at 1, 0.3065 at 2, 0.3181 at 10. The survival factor is f = 1 − A_los. The law reads redshift with distance as accumulation looked through; Hubble's law reads it as expansion. On the standard-candle distances the two readings agree, because the shared count RA₀ = 1/π fixes the same inventory (Chapter XII). They can part where a readout changes the two cosmological distances by different factors: distance duality D_L = (1+z)²D_A holds for any metric readout, and Chapter XII's diagnostic ratio g_L/g_A measures a departure from it. The chapter's differential test, dividing the comoving distance by f(z), shifts the inferred deceleration parameter by −6/π ≈ −1.91 at leading order. That is where a decider could live. None is registered; the law is carried as an idea with its decider named, not as a claim about data.

## For the Chapter I rework

After the sentence and the three objects: state the two numbers; give the bell as their picture with its question left open; state the result and its failed converse with the conjunction as the example; give GPS as the daily instance; then read the two numbers outward as the SAM law beside Hubble's law. The agreement theorem of note 1 supplies γ = 1 so that the road's delay is Σ/c exactly.

## Credit

Sean Brady: the magic bell and its placement (the clock deep in accumulation, the observer in the void at the floor), the result as an idea rather than an answer, the SAM law and its stance toward Hubble's law, the GPS origin. Claude Code: the proof, the converse and its Cassini instance, the GPS numbers, the reading of the law through Chapter XII's road law and differential test, the computation and this note.
