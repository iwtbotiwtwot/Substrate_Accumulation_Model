# Release record: core 0.11.1 / Duck 2.3.1 / IRONCLAD-R28, the feedback clock, 2026-10-20

**Kind:** permanent installed-version change (CLAUDE.md §13). Sean Brady: "proceed with your recommendations" then "Allow permanent changes, readback approved."
**Where:** ironclad main 161e591 (tag duck-2.3.1), history entry H002746, plan docs/CORE_0_11_1_PLAN.md, fixture qualification/fixtures/feedback_clock
(PREREGISTRATION.json, OFFLINE_PRECHECK.json, RUN_CHECK.json), run runs/duck/ironclad-r28-feedback-clock, qualification record QUALIFICATION_20261020T221702Z.json.

**What changed.** The feedback construction's evolution time is now the native end of its event history (sum of event count times coordinate time per
event), taken by result pointer, instead of a separately supplied time. A derived metric lapse N sets the coordinate time per event to 1/N and scales the
source block of the generator; the field block is unscaled. Without a history the legacy chart is byte-identical to the sealed 0.10.2. Malformed combinations
are refused at compile time. Two directories unchanged: the sealed 0.10.2 and 0.11.0.

**Conventions adopted by Sean Brady (labelled as conventions):** the lapse direction (coordinate time per source tick = 1/N) and N acting on the source block.

**Evidence.** Tests 151 OK before, 156 OK after; verify PASS at IRONCLAD-R28 / 2.3.1 / 0.11.1; offline precheck and the pre-registered Duck fixture both show
every expected relation: legacy equals 0.10.2 exactly; routed N = 1 equals legacy through one event and three intervals; lapses 4/5 and 16/25 at the same end
are pairwise disjoint from N = 1 in all state entries; the uncoupled source at 4/5 equals 0.10.2 at time 2/5 exactly; energy identity exactly zero; three
controls REFUSED as declared. Rollback to duck-2.3.0 verified before install. Independence: none (§8).

**Not decided:** which candidate lapse is a resting clock's proper time. Not a test of any volume. The exploration run explore_voli_threads stays staged.

Directed by Sean Brady. Executed with Claude Code.
