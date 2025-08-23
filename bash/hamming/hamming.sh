#!/usr/bin/env bash

main () {
	if [[ $# -ne 2 ]]; then
		echo "Usage: ${0##/} <string1> <string2>"
		exit 1
	fi

	local strand1="$1"
	local strand2="$2"

	if [[ ${#strand1} -ne ${#strand2} ]]; then
		echo "strands must be of equal length"
		exit 2
	fi

	local distance=0

	for (( i=0; i < ${#strand1}; i++ )); do
		local nucleotide1="${strand1:i:1}"
		local nucleotide2="${strand2:i:1}"

		if [[ "$nucleotide1" != "$nucleotide2" ]]; then
			((distance++))
		fi
	done

	echo "$distance"
}

main "$@"
