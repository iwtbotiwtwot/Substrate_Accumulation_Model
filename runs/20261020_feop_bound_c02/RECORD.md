# Run record: feop_bound_c02 (FEOP BOUND_C02 follow-up, peer run), 2026-10-20

**Kind:** research run (ideas and executed identities; no scientific claim; BOUND_C02 stays CANDIDATE).
**Where:** ironclad `campaigns/feop_bound_c02_20261020/` (TARGET.md, PREREGISTRATION.json, LIVE_CAPTURE.md, RUN_REPORT.md,
peers/*/{NOTES,REPORT}.md, results/RESULT_LEDGER.json, results/RUN_SHA256_MANIFEST.json); history entry H002737; run folder
`runs/duck/feop_bound_c02` (192 MB, out of git, manifest committed).
**Program:** Duck 2.1.1 / IRONCLAD-R25 (TEMPORARY result handles, H002736), GEN6 core 0.10.2; one 900 s window; four Opus peers
LOCAL, CRT, BOUND, REVIEW; lead outside the window, capturing leads live at Sean Brady's request.

**Direction (Sean Brady):** "FEOP first BOUND_C02 is the strongest proposed result: a fixed-prime-cutoff upper bound with a
logarithmic-depth remainder. LOCAL_R2 and CRT_EVEN_SEPARATION_CYLINDERS supply the strongest executable foundation." Four
questions set in TARGET.md: Selberg comparison, diameter, extend the local coverage, rebuild C02 rows by reference.

**Outcome:** COMPLETE, 74 returns, 74 COMPLETED, 0 FAILED. Every expectation written before a scan came out as written; two
self-caught emitter bugs are recorded. Reading, engineering register:

1. **C02 as a reduction.** At fixed z the sieve is a finite CRT product; Legendre's two-sided identity was executed natively on
   eight rows (to 16,807 cylinders, starts to 10^15). Selberg with the full divisor roster has exactly the Legendre normalizer;
   C02's d ≤ z roster gives a main term a constant factor above the true density (z7 0.3496 vs 0.2879). C02 wins only in
   remainder exponent and only at z=11 for g ≤ 25 (exact sign receipts).
2. **Local theory closed.** Non-recursive D_g(L) = 1 − (p−1)Σ min(g,h)p^(−2h) (two peers independently); pointwise mask identity;
   even separation 2s; an ultrametric tree formula for any tuple with even pairwise valuations, covering the nonselected primes;
   C02's (g+4/3)4^(−g) tail is the p=2 local excess at L=g.
3. **Diameter.** The nested offsets Q^(2i) are the wrong family; base-p⁴ digit tuples keep density near 2/7 with polynomial
   diameter; one count with every form inside the window was certified.
4. **New lead.** A depth-uniform two-sided bracket S_g ∈ X∏d_p(k) ± envelope, with k free, beats C02's upper bound 6.5× at
   X=4^16 (z7) and 1.22× at the other sizes; two steps remain host-side arguments.

**Failures:** no external sieve literature in the retrieval index (literature check unfinished); briefing text wrong on
`because` (own keys dropped by design); one path error in the authoring guide; shell-dictionary v1 wrong pointwise, fixed.

**Result handle (temporary change):** one live cross-controller use, COMPLETED with matching rank; every return carries a handle.
The temporary change ended with this run: ironclad main reverted to Duck 2.0.1 / IRONCLAD-R23 (H002738).

**Independence:** none (all Claude-authored, no external answer key).

Directed by Sean Brady. Executed with Claude Code (GEN6 Duck run feop_bound_c02, IRONCLAD-R25).
