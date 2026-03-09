#!/usr/bin/env bash
set -euo pipefail

OUT="${1:-website/src/data/whats-new.json}"
mkdir -p "$(dirname "$OUT")"

repos=(
  "/home/ben/Documents/projects/reasoningtool:reasoningtool"
  "/home/ben/Documents/projects/GOSM:GOSM"
  "/home/ben/Documents/projects/ARAW:ARAW"
)

tmp_ndjson="$(mktemp)"
trap 'rm -f "$tmp_ndjson"' EXIT

emit_commit() {
  local repo_label="$1"
  local hash="$2"
  local date="$3"
  local subject="$4"
  shift 4
  local files=("$@")

  local skills_csv
  skills_csv="$(printf '%s\n' "${files[@]}" | sed -nE 's#.*skills/([^/]+)/.*#\1#p' | sort -u | paste -sd, -)"
  local files_blob
  files_blob="$(printf '%s\n' "${files[@]}")"
  local type="general"
  if rg -q 'website/' <<< "$files_blob"; then
    type="website"
  elif rg -q 'claude-code-plugin/skills/' <<< "$files_blob"; then
    type="skills"
  elif rg -q 'src/scripts/' <<< "$files_blob"; then
    type="scripts"
  elif rg -q 'docs/|sessions/' <<< "$files_blob"; then
    type="docs"
  fi

  jq -n \
    --arg id "${repo_label}-${hash:0:10}" \
    --arg repo "$repo_label" \
    --arg date "$date" \
    --arg prompt "$subject" \
    --arg summary "$subject" \
    --arg type "$type" \
    --arg skills_csv "$skills_csv" \
    '{
      id: $id,
      repo: $repo,
      date: $date,
      prompt: $prompt,
      summary: $summary,
      type: $type,
      skills: (if ($skills_csv|length)==0 then [] else ($skills_csv|split(",")) end)
    }' >> "$tmp_ndjson"
}

for pair in "${repos[@]}"; do
  repo_path="${pair%%:*}"
  repo_label="${pair##*:}"
  [[ -d "$repo_path/.git" ]] || continue

  current_hash=""
  current_date=""
  current_subject=""
  declare -a current_files=()

  while IFS= read -r line; do
    if [[ "$line" == "@@@"* ]]; then
      if [[ -n "$current_hash" ]]; then
        emit_commit "$repo_label" "$current_hash" "$current_date" "$current_subject" "${current_files[@]}"
      fi
      payload="${line#@@@}"
      current_hash="${payload%%|*}"
      payload="${payload#*|}"
      current_date="${payload%%|*}"
      current_subject="${payload#*|}"
      current_files=()
    elif [[ -n "$line" ]]; then
      current_files+=("$line")
    fi
  done < <(git -C "$repo_path" log --no-merges -n 350 --date=short --pretty=format:'@@@%H|%ad|%s' --name-only)

  if [[ -n "$current_hash" ]]; then
    emit_commit "$repo_label" "$current_hash" "$current_date" "$current_subject" "${current_files[@]}"
  fi

done

jq -s '
  sort_by(.date, .repo) | reverse
  | to_entries
  | map(.value + {iteration: (.key + 1)})
' "$tmp_ndjson" > "$OUT"

echo "Wrote $OUT"
