# Concept note 3 — The clock in motion: position and speed add

Sean Brady, originator and conceptual director. ChatGPT, Codex and Claude as AI research collaborators; this note AI-assisted writing (Claude Code), 2026-10-30. The one-line clock and its GPS closure were proposed by web Claude on 2026-10-30 and relayed by Sean Brady; the corrections below are the lead's. Verification: Courtroom II case `voli_clock_motion/01_clock_in_motion`.

## In plain language

A clock in the halo has two reasons to run slow: where it sits and how fast it moves. Chapter IV's exact law is dτ/dt = √(1−a) √(1 − v_loc²/c²), with v_loc the speed a local static observer measures. For a clock moving along the sphere this is exactly √(1 − a − β²) with β the coordinate speed, and to first order it is 1 − a/2 − β²/2 for any motion. Position and speed add. That one line gives GPS: 45.7 microseconds a day from where the satellite sits, −7.2 from how fast it moves, 38.5 net, and 38.6 once the ground clock's own rotation is counted, which is the number engineered into the satellites. For a circular orbit the velocity term is exactly half the position term, β² = a/2, and the rate is √(1 − 3a/2) to the last digit; the circular family ends at the photon sphere, a = 2/3.

Where the clock stops is the line a + β² = 1. Light lives on that line with zero proper time: its coordinate speed in the halo is β² = 1 − a, which is the c_eff reading again. Mass alone reaches the line at a = 1, the end of the road; speed alone reaches it at β = 1. In SAM's words, velocity adds to accumulation, and closure is one line reached two ways.

The caveat is the most important sentence in the note. β is velocity relative to the frame in which the field is static, not velocity through the floor. If it were velocity through the floor, Earth's 370 km/s against the microwave background would offset every GPS clock by 66 milliseconds a day and modulate it through the year by 21 milliseconds a day, some ten million times what GPS timing tolerates. The term is absent. So the floor, having no gradient, defines no rest frame, and the formula is reciprocal: two observers in relative motion each read the other's accumulation raised by β², and neither is "really" moving.

## The law

In the frame in which the field is static:

dτ/dt = N √(1 − v_loc²/c²), N = √(1−a).

- Tangential motion in areal coordinates: dτ/dt = √(1 − a − β²), β the coordinate speed. Circular orbit: β² = a/2, dτ/dt = √(1 − 3a/2).
- First order, any motion: dτ/dt = 1 − a/2 − β²/2 (Chapter IV's weak-field clock law).
- Closure: a + β² = 1 (tangential coordinate speed); light sits on it. β = 1 with a > 0 gives N² = −a < 0, a line no worldline occupies: nothing is "past the edge".
- Escape from rest at infinity: v_loc² = a c² exactly at every radius (Chapter V's e = 1 infall); bound iff v_loc² < a c². In coordinate speed the bound condition reads β² < a(1−a); the circular orbit β² = a/2 lies inside both.

## GPS, the demonstration

| term | value |
|---|---|
| a at the ground (mean radius) | 1.39×10⁻⁹ |
| a in orbit (26 560 km) | 3.34×10⁻¹⁰ |
| β² in orbit (= a/2) | 1.67×10⁻¹⁰ |
| gravitational, per day | +45.7 µs |
| velocity, per day | −7.2 µs |
| net, non-rotating ground clock | +38.5 µs |
| ground rotation at the equator | +0.1 µs |
| net with rotating ground clock | +38.6 µs |

The two corrections are the clock's two terms; the road's correction (concept note 2) is separate and picoseconds.

## The frame caveat, as a control

| if β were velocity through the floor | value |
|---|---|
| β² for 370 km/s | 1.52×10⁻⁶ |
| rate offset β²/2 | 7.6×10⁻⁷ = 66 ms per day |
| annual modulation 2 β_CMB β_orb | 2.5×10⁻⁷ = 21 ms per day |
| GPS timing stability | order 10 ns per day |

Absent by seven orders of magnitude. Velocity is relative to the field's static frame; the floor defines none. (The proposal quoted 10⁻⁸ for this effect; the computed offset is 7.6×10⁻⁷ and the argument is the stronger for it.)

## Corrections to the proposal, recorded

1. Light sits on the closure line a + β² = 1, not at or past β = 1; "N² = −a" is spacelike.
2. The CMB figure is 7.6×10⁻⁷, not 10⁻⁸.
3. The clock shorthand uses the coordinate speed and the thresholds are exact in the local speed; the chapter states the exact law in the local speed and the shorthand as its tangential and first-order form.

## For the Chapter I rework

The chapter's readings become three: the clock, the ruler, and the clock in motion. After the two numbers of note 2: state the law, the circular-orbit identity, the closure line with light on it, the thresholds in the local speed, GPS as the demonstration, and the frame caveat with its control.

## Credit

Web Claude: the one-line clock, the GPS closure, the closure-line reading, the frame caveat and its reciprocity. Sean Brady: the direction, and the judgement that this is significant enough to carry into Courtroom II. Claude Code: the three corrections, the computation and this note.

## Follow-up, 2026-10-30 (Sean Brady: "Go on both")

Two verification cases were added to the campaign, both proposed by Claude Code.

**The frame caveat as a measured limit** (`voli_clock_motion/03_floor_frame_bound`). Suppose the clock carried a term k β_floor² with the floor the microwave-background frame. Clocks moving together cannot see it; the cross term with a clock's own velocity wobbles as the clock turns. At declared stabilities: ground optical clocks over a sidereal day give k < 5×10⁻⁹, the annual motion k < 8×10⁻⁹, and the GPS orbital motion only k < 9×10⁻⁶ (nanosecond residuals over a twelve-hour period are the weakest instrument). Zero is consistent, and the best bound is the order of the published Ives-Stilwell type limit on anomalous time dilation. The stabilities are inputs, stated as such. One sealed prediction missed: the lead wrote the GPS-orbital time-offset amplitude a thousand times too large, so the sealed bound read 10⁻⁸; the miss stands in the record unpatched.

**The GPS eccentricity correction** (`voli_clock_motion/04_gps_eccentricity`, HELD). Integrating the clock-in-motion law along an eccentric orbit, the periodic part is the operational correction F e √A sin E, with F = −2√μ/c² matching the interface specification's −4.442807633×10⁻¹⁰ s/√m to 9×10⁻¹¹ relative, amplitudes 11.4, 22.9 and 45.8 ns at eccentricities 0.005, 0.01 and 0.02, closing after each orbit; the constant part is the circular rate, 38.5 µs/day against the ground. One law gives both GPS corrections, and the periodic one tests the velocity term on its own.
