#!/usr/bin/env bash

usage() {
	echo "Usage: ${0##/} <person>"
}

hello() {
	echo "Hello, $1"
}

main () {
	if [[ $# -ne 1 ]]; then
		usage "$@"
		exit 1
	fi
	
	hello "$@"
}

main "$@"
