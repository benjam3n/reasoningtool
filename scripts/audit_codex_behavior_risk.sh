#!/usr/bin/env bash
set -euo pipefail

SKILLS_DIR="${1:-$HOME/.codex/skills}"

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "Skills directory not found: $SKILLS_DIR" >&2
  exit 1
fi

tmp_missing="$(mktemp)"
tmp_placeholders="$(mktemp)"
trap 'rm -f "$tmp_missing" "$tmp_placeholders"' EXIT

existing="$(for d in "$SKILLS_DIR"/*; do [[ -d "$d" ]] && basename "$d"; done | sort -u)"
invoked="$(rg --no-messages -n "INVOKE:" "$SKILLS_DIR" -g 'SKILL.md' \
  | sed -E 's/.*INVOKE:[[:space:]]*//g' \
  | sed -E 's/.*\$([A-Za-z0-9._-]+).*/\1/g; t; d' \
  | sort -u)"

comm -23 <(printf '%s\n' "$invoked" | sort -u) <(printf '%s\n' "$existing" | sort -u) > "$tmp_missing" || true

{
  rg --no-messages -n "INVOKE:\s*/|INVOKE:\s*\$\[" "$SKILLS_DIR" -g 'SKILL.md' || true
  rg --no-messages -n "INVOKE:.*(next_procedure|procedure_name|\$skill)\b" "$SKILLS_DIR" -g 'SKILL.md' || true
} > "$tmp_placeholders"

echo "CODEx Behavior Risk Audit"
echo "skills_total: $(rg --no-messages --files "$SKILLS_DIR" | rg 'SKILL\.md$' | wc -l)"
echo "missing_invoke_targets: $(wc -l < "$tmp_missing")"
echo "placeholder_or_slash_invokes: $(wc -l < "$tmp_placeholders")"
echo

if [[ -s "$tmp_missing" ]]; then
  echo "Missing invoke targets:"
  cat "$tmp_missing"
  echo
fi

if [[ -s "$tmp_placeholders" ]]; then
  echo "Placeholder/slash invoke lines:"
  cat "$tmp_placeholders"
  echo
fi

echo "High-impact orchestrator risk signals:"
for s in gosm pce gu gjs claim decide diagnose search evaluate how want next analyze action viability certainty iterate meta; do
  f="$SKILLS_DIR/$s/SKILL.md"
  [[ -f "$f" ]] || continue
  invoke_count="$( (rg --no-messages -n "INVOKE:" "$f" || true) | wc -l )"
  assume_count="$( (rg --no-messages -n "ASSUME RIGHT|ASSUME WRONG" "$f" || true) | wc -l )"
  echo "$s invoke=$invoke_count assume_branches=$assume_count"
done
