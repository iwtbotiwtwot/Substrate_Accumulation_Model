# Focused approved-render visual QA

Inspected `qa/approved/page-6.png`, `page-26.png` and `page-41.png` at original/native resolution using `tools.view_image`, emitting and viewing all three actual PNGs. No manuscript, DOCX, PDF or image was edited.

| Page | Check | Result |
|---:|---|---|
| 6 | Source census, formulas, cleaned filename, header/footer | PASS. All content fits; no escape residue, clipping or overlap. |
| 26 | Custody-deviation text and cleaned field assignment | PASS. `same_run_repair = false` is visible and correct; no escaped markup remains. Layout and footer are clean. |
| 41 | Ground-state multiplicity and entropy table | Correction required. Ground M header and entropy decimals now fit, and exact multiplicities remain complete. However, the first three ground-energy values wrap their final digit onto a second line. |

Page 41 exact locations: the first three positive-fill rows display `-1,999,00` then `0`, `-1,998,20` then `0`, and `-1,998,06` then `8`. The ground-energy column needs slightly more width or a small font/format adjustment. The table cannot yet receive an unqualified clean-typography confirmation. No data are missing, and no black boxes, clipping, overlap or footer collisions were observed.

The parent was notified promptly of the remaining ground-energy wrap. Other approved pages in the previous review range were not reread here because the parent supplied a pixel-equivalence confirmation with a retained manifest; footer-only checks are assigned separately.
