#!/usr/bin/env sh
set -eu

test -f repo-catalog/repositories.yaml
test -f repo-catalog/dependency-map.yaml
test -f repo-catalog/ownership-map.yaml
test -f repo-catalog/maturity-map.yaml

grep -q "00-kdd-governance" repo-catalog/repositories.yaml
grep -q "17-digital-twin-simulation-lab" repo-catalog/repositories.yaml

echo "repo catalog ok"

