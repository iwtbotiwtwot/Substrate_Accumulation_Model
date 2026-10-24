# Run record — core 0.11.3 / Duck 2.3.5 / IRONCLAD-R32 install and its fixture run

- **Date (UTC):** 2026-10-24; prepared 15:xx–16:3xZ on branch `core-0.11.3`; minted 18:50:55Z; fixture probe 18:52:38Z–19:02:38Z; installed commit 19:1xZ.
- **Directed by:** Sean Brady ("make the permanent changes for the derivation …"; "Allow permanent changes, readback approved"). **Executed with:** Claude Code.
- **Where it ran:** ironclad branch `core-0.11.3` (f2d8c03e, PREPARED), merge 19397c0d, release commit `bdfbd21d`, history entry `H002779`, tag `duck-2.3.5`; fixture run
  `runs/duck/core_0_11_3_fixture` (600 s probe, root submissions, no peers); readback `docs/CORE_0_11_3_PLAN.md`; qualification `qualification/QUALIFICATION_20261024T190719Z.json`
  (an earlier record at 190517Z captured a stale verify before `installed --write` and is retained); freeze `docs/DUCK_2.3_5_FREEZE.json`; rollback `docs/DUCK_2.3_5_ROLLBACK_CHECK.json`.
- **Installed version:** Duck 2.3.5 / IRONCLAD-R32 / core 0.11.3 beside 0.11.2, 0.11.1, 0.11.0 and the sealed 0.10.2; permanent; rollback target duck-2.3.4 verified PASS before install.
- **What ran:** the §13 procedure in order: plan and diff on a branch; 182 unit tests OK; the fixture pre-registered and executed natively offline before install (all relations
  hold); rollback verified; the phrase typed and the readback approved; merge; mint; verify PASS; the fixture through the Duck on the installed machine; qualification; freeze; tag.
- **What it showed** (engineering labels):
  - **Fixture COMPLETE as registered:** 5 COMPLETED (unfloored reservoir; floored reservoir at two times; the line of sight at exponent 3 and at exponent 2) and 3 REFUSED_AS_DECLARED
    (exponent 0; floor 1; descending path). On the Duck receipts: the unfloored reservoir equals 0.11.2; floor residual and law residuals enclose 0 at 1e-47; the regression is exactly
    (21/22, −21/11, 35/11) at d = 3 and (7/11, −21/22, 14/11) at d = 2; q_res, q_obs, Λ_obs and the closed-form delay enclose their closed forms.
  - **What the two objects are:** declared constitutive laws (a floor beside the reservoir; conservation of the ruler density per comoving volume along a line of sight), in the same
    standing as the reservoir's constant-impedance law. They derive nothing; the construction's `derivation` readout is OPEN.
- **What failed, plainly:** the first qualification record captured a verify FAIL from a stale INSTALLED.json (authority files changed before `installed --write`); rerun PASS. Nothing else.
- **What it changes or opens in the volumes:** none in the text; the volume's drafted ceiling section §7 already names these two constructions as "what would derive the ceiling"
  and that paragraph remains accurate: they now exist natively, and the derivation is the object still unwritten. Register entries T-02/T-03/T-10 gain their native instrument.
- **Ideas logged:** none new (the runs that would use the constructions are in `ideas/IDEAS.md` under voli_ceiling_1–3).
- **Concluded by:** `scripts/conclude.sh` on 2026-10-24 (hash in the commit).
