#!/usr/bin/env bash
#
# Lab matrix: every lab's vulnerable variant must FAIL for its forbidden
# outcome, and its fixed variant must PASS.
#
#   bash scripts/run_labs.sh          # every lab
#   bash scripts/run_labs.sh 4.3 5.2  # named modules only
#
# Dependencies are installed per lab before anything is asserted. Without that,
# a missing package reports as a test failure that is not a test failure --
# labs/5.2 needs `cryptography` and otherwise shows six errors that look like
# a broken fixture.

set -uo pipefail

cd "$(dirname "$0")/.." || exit 2
PY="${PYTHON:-python3}"
FILTER=("$@")

pass=0; fail=0; skipped=0
declare -a FAILURES=()

in_filter() {
  [ ${#FILTER[@]} -eq 0 ] && return 0
  local want="$1" f
  for f in "${FILTER[@]}"; do [ "$f" = "$want" ] && return 0; done
  return 1
}

printf '%-34s %-10s %-10s %s\n' LAB VULNERABLE FIXED RESULT
printf '%s\n' "----------------------------------------------------------------------"

for conftest in labs/*/*/conftest.py; do
  lab="$(dirname "$conftest")"
  module="$(basename "$(dirname "$lab")")"
  in_filter "$module" || continue

  # Install first, but do not treat a failed install as a lab defect: the
  # environment may already satisfy the pin under a system package manager that
  # pip refuses to touch. Only if a variant then misbehaves does the install
  # error become the explanation.
  dep_note=""
  if [ -f "$lab/requirements.txt" ]; then
    if ! dep_out="$("$PY" -m pip install -q -r "$lab/requirements.txt" 2>&1)"; then
      dep_note="$(printf '%s' "$dep_out" | grep -m1 -i error || echo 'pip install failed')"
    fi
  fi

  # Most labs select a variant with --impl. labs/1.1 still takes --claim and a
  # path to a claim file; it is queued for migration (lab-realism.mdc).
  if grep -q '"--impl"' "$conftest"; then
    vuln_cmd=("$PY" -m pytest "$lab/tests" --impl vulnerable -q)
    fixed_cmd=("$PY" -m pytest "$lab/tests" --impl fixed -q)
  elif grep -q '"--claim"' "$conftest"; then
    vuln_cmd=("$PY" -m pytest "$lab/tests" -q --claim "$lab/vulnerable/security_claim.yaml")
    fixed_cmd=("$PY" -m pytest "$lab/tests" -q --claim "$lab/fixed/security_claim.yaml")
  else
    printf '%-34s %-10s %-10s %s\n' "$module" - - "SKIP (no variant flag)"
    skipped=$((skipped + 1)); continue
  fi

  "${vuln_cmd[@]}" >/dev/null 2>&1 && vuln=passed || vuln=failed
  "${fixed_cmd[@]}" >/dev/null 2>&1 && fixed=passed || fixed=failed

  result=OK; broken=0
  # The vulnerable variant passing means the tests do not assert the property.
  if [ "$vuln" = passed ]; then
    result=BROKEN; broken=1
    FAILURES+=("$lab: vulnerable variant PASSED; the tests do not assert the forbidden outcome")
  fi
  if [ "$fixed" = failed ]; then
    result=BROKEN; broken=1
    if [ -n "$dep_note" ]; then
      FAILURES+=("$lab: fixed variant FAILED, and dependencies did not install ($dep_note). Fix the environment before reading this as a lab defect.")
    else
      FAILURES+=("$lab: fixed variant FAILED; run '${fixed_cmd[*]}' to see why")
    fi
  fi
  [ -n "$dep_note" ] && [ "$broken" -eq 0 ] && result="OK (deps preinstalled)"

  printf '%-34s %-10s %-10s %s\n' "$module" "$vuln" "$fixed" "$result"
  if [ "$broken" -eq 0 ]; then pass=$((pass + 1)); else fail=$((fail + 1)); fi
done

echo
echo "labs ok: $pass   broken: $fail   skipped: $skipped"

if [ ${#FAILURES[@]} -gt 0 ]; then
  echo
  echo "Anomalies:"
  for f in "${FAILURES[@]}"; do
    echo "  - $f"
    echo "::error::$f"
  done
  exit 1
fi
