#!/usr/bin/env python3
"""F3 + F4 (+F5, F8) pass on Chapter I and Appendix A, expanded version (Sean Brady, 2026-11-02: "go on the expanded version";
the 30 October statement treated as an idea on record, not direction for the text). One vocabulary: the ruler reads dr/sqrt(1-a);
the optical road is int dr/(1-a) = c times light's coordinate time (c_eff along the road); "measurable" survives only inside the
July quotation. Section 4 gains light as the third reading of the lift (H001672); Section 6.3 the GPS pair (H001702); Section 3 the
Sigma element (H002043); Section 9 the postulate stated as declared; Section 11 the register; Appendix A one sentence. Applied to
ch01_concepts.tex and its derived body01_concepts.tex, and closure_appendix.tex. Each replacement asserted once per file; logged."""
import json, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent; LOG = []
def rep(path, old, new):
    p = ROOT / path; s = p.read_text(); n = s.count(old)
    if n == 0 and s.count(new) >= 1:
        LOG.append({"file": path, "old": old[:200], "new": new[:200], "note": "already applied by an earlier run"}); return
    assert n == 1, f"{path}: expected 1 of {old[:80]!r}, found {n}"
    p.write_text(s.replace(old, new)); LOG.append({"file": path, "old": old[:200], "new": new[:200]})
E = [
 # Section 3: the Sigma element (F8)
 ("where $a$ is the local lift and $\\dd\\ell$ the measurable length element along the route.",
  "where $a$ is the local lift and $\\dd\\ell$ the length element along the route, the ruler's reading of Section~\\ref{sec:c1-readings}; to first order in $a$ the accumulation looked through is insensitive to which element is used, and the difference between routes of equal integrated accumulation begins at second order (H002043)."),
 # Section 4: three readings
 ("\\section{Two readings of the lift}", "\\section{Three readings of the lift}"),
 ("Physics enters when an instrument reads it, and SAM declares two readings.", "Physics enters when an instrument reads it, and SAM reads it three ways: with a clock, with a ruler, and with light."),
 ("and this is the static exterior of a spherical source in SAM.\n",
  "and this is the static exterior of a spherical source in SAM.\n\n\\paragraph{Light.} Light's coordinate speed where the lift is $a$ is $c_{\\rm eff}=c(1-a)$, the speed along the road; its speed measured locally is $c$. Integrated along a radial route this reading gives the optical road,\n\\begin{equation}\nL_{\\rm opt}=\\int\\frac{\\dd r}{1-a},\n\\label{eq:c1-optical-road}\n\\end{equation}\nwhich is $c$ times the coordinate time light takes, as distinct from the ruler's length $\\int\\dd r/\\sqrt{1-a}$ along the same route. The three readings are one object: a single generator with $g=\\sqrt{1-a}$ gives the clock rate $g$, the ruler $\\dd r/g$ and light's coordinate speed $g^2c$ (H001672). Where the ruler's length and the optical road part company is the subject of Section~\\ref{sec:c1-home}.\n"),
 # Section 6.2: the ruler's distance
 ("The first is the measurable distance of the route,", "The first is the ruler's distance along the route,"),
 ("\\end{equation}\nwhat a ruler laid along it reads. The second is the accumulation looked through,", "\\end{equation}\nThe second is the accumulation looked through,"),
 # Section 6.3: the GPS pair
 ("small because the Earth's hill is low, present because the route crosses it.",
  "small because the Earth's hill is low, present because the route crosses it. The two lengths of Section~\\ref{sec:c1-readings} also part here, by a hair: on the overhead link the radar distance read on the ground clock and the ruler's length integrated along the path differ by $7.7$~mm, the one $1.4$~mm below the straight chord and the other $6.3$~mm above it (H001702)."),
 # Section 9.1
 (" This is a theoretical departure, and it is the headline of the volume, not something to be hidden. It is also structural. It is not a statement about speed or time, and no engine, however fast, changes it. Every observer approaches the boundary; none crosses.",
  " This is a theoretical departure, and it is the headline of the volume, not something to be hidden. It is SAM's declaration: every observer approaches the boundary; none crosses. What makes it hold for a traveler's own clock is the postulate of Section~\\ref{sec:c1-approach}."),
 # Section 9.2
 ("\\subsection{The approach, in SAM's accounting}\n",
  "\\subsection{The approach, in SAM's accounting}\n\\label{sec:c1-approach}\n\nThe departure is confined to the approach to $A=1$, where $a+\\beta^2\\to1$. Wherever Cassini, GPS and the binary pulsars look, motion is geodesic in the metric~\\eqref{eq:c1-metric} and the agreement theorem holds.\n"),
 ("The distance that decides whether a crossing completes is the measurable road, the distance a ruler built from the field reads, published in July 2026 and carried into Chapter~V. Along the approach that road is",
  "The distance SAM reads along the approach is the optical road of Section~\\ref{sec:c1-readings}, $c$ times the coordinate time light takes, published in July 2026 as the measurable road and carried into Chapter~V. Along the approach it is"),
 ("while the metric's own length to the horizon stays finite", "while the ruler's length to the horizon stays finite"),
 ("An astronaut cannot travel at $c$. The least time his own clock can spend on each nine of road is therefore the road at light speed, $r_s\\ln10/c$, and a traveler of any mass spends more. The total is unbounded in either case.",
  "SAM declares the road-speed postulate: a traveler's own time per unit of optical road is bounded below by light's, $\\dd L/\\dd\\tau\\le c$. Under it the least time his own clock can spend on each nine is $r_s\\ln10/c$, a traveler of any mass spends more, and the total is unbounded."),
 # Section 9.3
 ("SAM does not accept that accounting as the physical one, for the reason Section~\\ref{sec:c1-two} gave: the metric's length and the measurable road are two different numbers between the same endpoints",
  "SAM's declaration selects the other, for the reason Section~\\ref{sec:c1-two} gave: the ruler's length and the optical road are two different numbers between the same endpoints"),
 ("Road accumulation is local and is experienced; in SAM's accounting there is always more measurable distance ahead", "Road accumulation is local and is experienced; in SAM's accounting there is always more optical road ahead"),
 # Section 9.4
 ("The road to $A=1$ is infinite in measurable distance. Assuming the astronaut cannot travel at the speed of light, he will never experience reaching the horizon.",
  "The optical road to $A=1$ is infinite. Under the road-speed postulate a traveler never experiences reaching the horizon; the free-fall accounting, which SAM does not adopt, arrives in finite own time. Which is physical is decided by the law of motion Chapter~V owes, not by anything measured outside."),
 # Table caption
 ("SAM: the least possible own time per nine added to $A$, the road at light speed;", "SAM, under the road-speed postulate: the least own time per nine added to $A$, the optical road at light speed;"),
 # Section 10 map
 ("the criterion for a finite or infinite own time, the measurable road, and the bound", "the criterion for a finite or infinite own time, the optical road, and the bound"),
 # Section 11 register
 ("the divergence of the measurable road; the criterion for the traveler's own time.", "the divergence of the optical road."),
 ("\\emph{Declared}: the radial ruler reading, tested by Cassini; the source-only convention for the floor; the road-speed postulate at the boundary.",
  "\\emph{Declared}: the radial ruler reading, tested by Cassini; the source-only convention for the floor; the closed sphere with no interior; the road-speed postulate at the boundary, which makes the traveler's non-arrival follow."),
 ("How fast a traveler of a given mass covers the measurable road, and so how much longer", "How fast a traveler of a given mass covers the optical road, and so how much longer"),
 ("the law of motion for mass on the measurable road;", "the law of motion for mass on the optical road;"),
 ("under the declared readings and through the measurable road (\\texttt{g11555r/01}", "under the declared readings and through the optical road (\\texttt{g11555r/01}"),
 ("These are reproductions with standard tools, not independent verification in the sense of Appendix~A, and nothing in this chapter is classified.",
  "These are reproductions with standard tools, not independent verification in the sense of Appendix~A, and nothing in this chapter is classified. The native record behind the two lengths is H001672, H001695, H001702 and H002043 (September 2026), which construct the clock, the ruler and the optical road from one generator and measure the two lengths' difference on the GPS link."),
]
for f in ("ch01_concepts.tex", "body01_concepts.tex"):
    for old, new in E: rep(f, old, new)
rep("closure_appendix.tex", "No universal infinite-cost crossing rule follows independently.",
    "No universal infinite-cost crossing rule follows independently. Chapter~I declares the road-speed postulate (Section~9.2); under that declaration the non-arrival of a massive traveler is unconditional, and without it the resolution is the conditional one stated here.")
json.dump({"written_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "replacements": LOG}, open(ROOT / "checks" / "f3f4_pass_20261102.json", "w"), indent=1)
print(len(LOG), "replacements applied")
