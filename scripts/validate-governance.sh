#!/usr/bin/env sh
set -eu

required="README.md AGENTS.md design.md organization-map.md kdd-lifecycle.md agentic-operating-model.md repository-standards.md contribution-guide.md glossary.md"

for file in $required; do
  test -f "$file" || {
    echo "missing required file: $file" >&2
    exit 1
  }
done

echo "governance structure ok"

