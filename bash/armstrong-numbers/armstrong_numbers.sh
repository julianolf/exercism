#!/usr/bin/env bash

main () {
	if [[ $# -ne 1 ]]; then
		echo "Usage: ${0##/} <number>"
		exit 1
	fi

	local number=$1
	local exp=${#number}
	local digit=0
	local result=0
	local sum=0
	local i=0

	for ((i; i < exp; i++)); do
		digit=${number:i:1}
		result=$((digit ** exp))
		sum=$((sum + result))
	done

	if [[ $sum -eq $number ]]; then
		echo "true"
	else
		echo "false"
	fi
}

main "$@"
