# Independent check of principal N5000 and prime event claims

## Outcome

The requested headline claims in `manuscript/n5000_chapter.md` and `manuscript/prime_main.md` agree with the actual retained source records. No correction is required to those claims. This check read the original source JSON and design records directly, rather than accepting another worker's summary. It performed integer aggregation and scalar transcription arithmetic only. No scientific experiment, trajectory, source solve or bulk archive decompression was run.

Source root for the relative paths below is `/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/`.

## N5000 primary measure and archive

Read `GEN4/spin_n5000_archive1/ARCHIVE_MANIFEST.json` and independently flattened `shards[*].logical_rows`. That produces 192 logical rows: 96 with `case.orientation == K_MAJOR` and 96 with `case.orientation == T_MAJOR`. Grouping by `(case.family, case.fill, state)` produces exactly 96 pairs. Every pair has one row in each encoding, equal `records` and equal `joint_row_sha256`. Every source case has all sixteen `state` values from zero through fifteen in its primary rows.

The independently summed primary counts are:

| Source | Fill | K_MAJOR record sum |
|---|---:|---:|
| packet | +1 | 79,952 |
| packet | -1 | 461,138,212 |
| signed_packet | +1 | 63,968,000 |
| signed_packet | -1 | 461,223,474 |
| signed_packet_chain | +1 | 76,796,480 |
| signed_packet_chain | -1 | 467,053,874 |
| Total | | 1,530,259,992 |

These match the chapter table exactly. The nomenclature is three named packet families times two fill signs, yielding six specified sources. The manuscript correctly uses that distinction. Six sources times sixteen boundaries gives 96 measures; retaining both exponent encodings gives 192 logical rows and 96 comparison pairs. The primary total counts each joint measure once.

The unordered pair count is the exact arithmetic identity `5000 * 4999 / 2 = 12,497,500`, matching the chapter. Source completeness and the two fill choices are specified in `GEN4/spin_gpu_n5000_1/prepare.py` and the production specification `README.md`.

The archive manifest has 89 entries in `shards`; their `bytes` sum to 609,671,270,157, and their `raw_bytes` sum to 1,045,145,366,546. These equal the top-level `unique_shards`, `compressed_bytes` and `raw_bytes` values. The top-level compression `seconds` is 1260.6110792160034, matching the rounded 1,260.611 seconds in the manuscript.

Production runtime 2,824.215 seconds is directly recorded in `GEN4/spin_n5000_archive1/README.md`, lines 3 through 6, together with completion of 192 rows and 96 pairs, the 89 unique contents, and decompression checks against raw SHA256. The chapter correctly attributes one completed execution under its specified machine conditions and does not turn that timing into an asymptotic scaling law. The production result identity is bound by `GEN4/spin_n5000_archive1/BINDING.json`, field `production_result_sha256`, and the manifest's `result_sha256`.

The later custody claim is supported by actual completed receipts, rather than the older archive README's held-download status:

- `GEN4/spin_n5000_drive12_1/RESULT.json`: status `PASS_DRIVE_SHA256_AND_SIZE`; batches 1 and 2; 24 shards; 202,360,997,829 bytes; all 24 SHA256 values match.
- `GEN4/spin_n5000_t500_download1/RESULT.json`: status `COMPLETE`; batches 1 through 4; 57 verified shards and 405,775,215,862 verified bytes.
- `GEN4/spin_n5000_final_download1/RESULT.json`: status `COMPLETE`; batches 5 and 6; 32 verified shards and 203,896,054,295 verified bytes.
- `GEN4/spin_n5000_final_download1/READY_FOR_STORAGE_SHUTDOWN.json`: Drive batches 1 and 2 and T500 batches 3 through 6 are the retained final custody assignment.

The two completed download totals give `57 + 32 = 89` shards and `405,775,215,862 + 203,896,054,295 = 609,671,270,157` bytes. The manuscript explicitly states that these are retained verification receipts, without claiming a fresh reread of the full archive during revision.

## Prime event matched and fresh results

Read `GEN4/prime_balance1/COMPARISON.json`. Its top-level `tasks_scored` is 128 and `all_billion_complete` is true. Select `rows[*]` at `horizon == 1000000000`:

| Profile | Baseline false | Baseline missed | Balanced false | Balanced missed | Baseline exact | Balanced exact | Improved equal worsened |
|---|---:|---:|---:|---:|---:|---:|---|
| uniform | 271 | 13 | 17 | 3 | 1 | 47 | 62 1 1 |
| rough | 272 | 13 | 17 | 3 | 1 | 47 | 62 1 1 |

Each row has 64 seeds, matching the manuscript's one of 64 to 47 of 64 per profile. Independent aggregation of `pairs[*]` agrees with the exact-sequence counts. The old total is `271 + 13 + 272 + 13 = 569`; the new total is `17 + 3 + 17 + 3 = 40`. The reduction is exactly `(569 - 40) / 569 * 100 = 92.97012302284709` percent, correctly rounded to 92.9701 percent.

Read `GEN4/prime_balance1/HOLDOUT_ANALYSIS.json`. Both `uniform` and `rough` record 16 seeds, 2 false emissions, 1 missed prime and thirteen names in `exact_seeds`. `exact_by_horizon[1000000000]` is thirteen in both profiles. The `scope` field explicitly identifies sixteen new seed pairs with disjoint base and auxiliary RNG ranges and no paired baseline runs. `profile_differences` is empty. This matches the chapter's fresh continuation and its paired-profile interpretation.

The archive custody statements match `GEN4/prime_balance1/FINAL_VERIFIED.json` and `HOLDOUT_VERIFIED.json`: both statuses are `PASS`, with 26,220 files and 25,821,384,418 bytes for the original archive, and 6,535 files and 6,350,494,109 bytes for the fresh archive. This check read those verification results; it did not repeat their bulk hash campaign.

## Prospective algebra and resource conventions

The planned source change is stated in `GEN4/prime_balance1/DESIGN.md`, lines 3 through 15: keep the topology and pair strength, change the four triple rows and their hidden fields until the effective coefficients satisfy `b = a`, and select the target algebraically before examining new sequences. Lines 17 through 22 retain beta one, Gamma 512, the cadence profiles, three readings, streams and complete matched seed roster. The initially planned horizon is 100 million; `POD_PLAN.md` explicitly extends the same frozen source and roster toward one billion. `REPORT.md` records completion. The chapter preserves that planned intervention and observed-result distinction.

`GEN4/prime_balance1/DERIVATION.md`, lines 3 through 32, supplies the source-only derivation. At fixed positive a, `min(b, 2a-b) <= a`, with equality exactly at `b = a`. With `C = cosh(8)` and `z = cosh(2t)^2`, the equation becomes `z^2 = C(2z-1)`. Its admissible positive-strength root gives `t = acosh(sqrt(C + sqrt(C^2-C))) / 2`. Direct scalar arithmetic returns `t = 2.346489729898476` and `a = b = 3.6534264659876117`, agreeing with the retained binary64 source output at displayed precision. This is a maximum of the weaker static margin, not a universal optimum for whole-trajectory survival.

Read the attached prime-event paper's Section V A, equations 20 and 21, and Table V. The source budgets are `B_J = 4u + 12t` and `B_Jeta = 4u + 16t`. At `u = 4` and the balanced t, independent arithmetic gives 44.15787675878171 and 53.543835678375615, correctly rounded in the manuscript to 44.157877 and 53.543836. Relative increases are 10.394691896954278 percent and 11.549657663282531 percent. The 17.324486494923796 percent change applies to t alone. These are dimensionless strength conventions, as the chapter states.

The manuscript's resource-control ranking agrees with that paper: the balanced source's predicted survival is approximately 0.717; uniform strengthening gives approximately 0.708 at matched coupling budget and approximately 0.770 at matched coupling-plus-field budget. The four-reading baseline control is approximately 0.774 at unchanged total exposure. The chapter correctly identifies these as numerical control predictions separate from the observed 64-seed and 16-seed ensembles. The original balanced campaign itself did not hold the total strength budget fixed.

## Presentation and scope

Both chapter openings lead with completed constructions and substantive results. N5000 opens with the six complete joint measures and their primary record count; prime event opens with the measured matched and fresh trajectory improvements. Their relevant closing passages retain those successes and state the precise model and return objects.

The N5000 joint-density section does not claim a universal solver for arbitrary dense graphs or a runtime exponent. Its subsequent thermal result names its separately normalized family and first-onset theorem; this bounded check did not rederive that theorem. Prime event distinguishes an exact finite realized decision sequence from an arbitrary-input primality certificate or an unbounded stochastic guarantee. It does not infer an equivalence with FEOP. The resource section keeps static margin optimization separate from total trajectory survival and gives the actual budget-dependent ranking.

No requested headline transcription or scope error was found. Rendering corrections identified in the separate visual QA report remain a separate production task for the parent agent.
