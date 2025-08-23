#!/usr/bin/env bash

set -o errexit
set -o nounset

main() {
    [[ $# -gt 0 ]] && name="$1" || name="you"

    echo "One for $name, one for me."
}

main "$@"
