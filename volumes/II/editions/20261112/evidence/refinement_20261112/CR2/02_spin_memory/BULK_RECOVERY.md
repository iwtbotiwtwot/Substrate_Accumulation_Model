# Public data recovery

Large raw operands remain on the T500 and are hash-committed in MANIFEST.json.
Their verified lossless archive parts are committed under public_bulk/. The
complete file roster, sizes and hashes are in RESULTS/PUBLIC_BULK_INDEX.json.
No source/result is dropped or covered by a new ignore rule.

After cloning, restore the exact raw operands with standard Python:

    python3 scripts/restore_bulk.py

Verify all archive bytes without restoring with --verify-only. The restorer
checks every part and member, refuses symlink traversal and never overwrites a
different existing file. It writes no receipt into the immutable case. Public
engine-free reproduction uses these recovered operands and the retained replay
instructions; no private ironclad mount, live engine or Drive archive is needed.
