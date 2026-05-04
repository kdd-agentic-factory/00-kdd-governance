#!/usr/bin/env sh
set -eu

for file in templates/*.template.md; do
  test -s "$file" || {
    echo "empty template: $file" >&2
    exit 1
  }
done

echo "templates ok"

