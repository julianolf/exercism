#!/usr/bin/env bash

usage() {
	echo "Usage: error_handling.sh <person>"
}

hello() {
	echo "Hello, $1"
}

main () {
	if [[ $# != 1 ]]; then
		usage
		exit 1
	fi

	hello "$1"
}

main "$@"
