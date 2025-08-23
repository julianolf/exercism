#!/usr/bin/env bash

main () {
	if [[ $# -ne 1 ]]; then
		echo "Usage: ${0##/} <number>"
		exit 1
	fi

	local number=$1
	local result=""


	if [[ $((number % 3)) -eq 0 ]]; then
		result="Pling"
	fi

	if [[ $((number % 5)) -eq 0 ]]; then
		result="${result}Plang"
	fi

	if [[ $((number % 7)) -eq 0 ]]; then
		result="${result}Plong"
	fi

	if [[ -z $result ]]; then
		result="$number"
	fi

	echo "$result"
}

main "$@"
