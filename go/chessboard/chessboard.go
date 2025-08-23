package chessboard

type File []bool

type Chessboard map[string]File

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file.
func CountInFile(cb Chessboard, file string) int {
	var c int

	if f, ok := cb[file]; ok {
		for _, v := range f {
			if v {
				c++
			}
		}
	}

	return c
}

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank.
func CountInRank(cb Chessboard, rank int) int {
	var c int

	if rank >= 1 && rank <= 8 {
		for _, f := range cb {
			if f[rank-1] {
				c++
			}
		}

	}

	return c
}

// CountAll should count how many squares are present in the chessboard.
func CountAll(cb Chessboard) int {
	var c int

	for range cb {
		c += 8
	}

	return c
}

// CountOccupied returns how many squares are occupied in the chessboard.
func CountOccupied(cb Chessboard) int {
	var c int

	for f := range cb {
		c += CountInFile(cb, f)
	}

	return c
}
