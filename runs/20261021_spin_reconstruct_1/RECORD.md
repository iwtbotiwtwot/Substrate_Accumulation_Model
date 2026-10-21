# Run record: spin_reconstruct_1 (false start: blind rebuild, replaced by spin_verify_1), 2026-10-21

**Kind:** staged research run, not executed (no submissions). Duck 2.3.4 / IRONCLAD-R31 / core 0.11.2.
**Where:** ironclad `campaigns/spin_reconstruct_1_20261021/` (FALSE_START.md, TARGET.md, prior/DEFINITIONS.md, sealed/); run folder `runs/duck/spin_reconstruct_1`
(window opened empty 21:41Z, stopped 21:50:50Z). The sealed headline file was held here (`sealed/SEALED_HEADLINES.json`, commit 5616960) and its hash in
ironclad; the file has since been copied into the ironclad campaign with its hash confirmed.

**What it was:** a blind rebuild of five spin results with the values sealed by SHA-256 and the peers forbidden the earlier campaign directories.
**Why it was replaced (Sean Brady):** "we are asking the peers to verify something and not giving it to them?"; "Is the a smarter way that is less like a test
and more like a verification?" The replacement, spin_verify_1, gives the peers everything and takes its strength from separate code, exhaustive optima,
the explanation as a native ordering, predictions written before computing, and break attempts (`runs/20261021_spin_verify_1/RECORD.md`; decision in
`decisions/DECISIONS.md`, 2026-10-21).

Directed by Sean Brady. Executed with Claude Code.
