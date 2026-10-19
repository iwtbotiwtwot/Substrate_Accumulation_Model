#!/usr/bin/env bash
# End-of-run procedure (CLAUDE.md §2): refresh hashes, check run records, commit, sync. Usage: scripts/conclude.sh "message"
set -euo pipefail
cd "$(dirname "$0")/.."
msg="${1:-}"; [ -n "$msg" ] || { echo "usage: scripts/conclude.sh \"<commit message>\""; exit 2; }
missing=0
for d in runs/*/; do [ -d "$d" ] || continue; [ -f "$d/RECORD.md" ] || { echo "missing RECORD.md in $d"; missing=1; }; done
[ "$missing" = 0 ] || { echo "write the run record first (templates/RUN_RECORD.md)"; exit 3; }
big=$(git ls-files -z --others --exclude-standard --cached | xargs -0 -I{} sh -c 'test -f "{}" && test $(stat -c %s "{}") -gt 10485760 && echo "{}"' 2>/dev/null || true)
[ -z "$big" ] || { echo "files over 10 MiB are bulk and stay out of this repository:"; echo "$big"; exit 4; }
{ git ls-files -z; git ls-files -z --others --exclude-standard; } | sort -zu | grep -zv '^SHA256SUMS$' | xargs -0 sha256sum > SHA256SUMS
git add -A
if git diff --cached --quiet; then echo "nothing to commit"; else
  git commit -q -m "$msg

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
fi
if git push -q -u origin "$(git branch --show-current)" 2>/dev/null; then echo "synced: $(git log -1 --format=%h) on $(git branch --show-current)"; else
  echo "push refused in this environment; run:  ! git -C $(pwd) push -u origin $(git branch --show-current)"; exit 5; fi
