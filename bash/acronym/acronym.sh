#!/usr/bin/env bash

main () {
	if [[ $# -ne 1 ]]; then
		echo "Usage: ${0##/} <string>"
		exit 1
	fi

	echo "$1" | sed 's/[^a-zA-Z -]//g;s/[ -]/\n/g' | cut -c1 | tr -d '\n' | tr '[:lower:]' '[:upper:]'
}

main "$@"
