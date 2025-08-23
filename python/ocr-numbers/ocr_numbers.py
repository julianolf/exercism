ROW_SIZE = 4
COL_SIZE = 3

numbers = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}


def convert(input_grid):
    if len(input_grid) % ROW_SIZE != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if any(len(columns) % COL_SIZE != 0 for columns in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    digits = []

    for r_idx in range(0, len(input_grid), ROW_SIZE):
        rows = input_grid[r_idx:r_idx+ROW_SIZE]
        cols = []

        for c_idx in range(0, len(rows[0]), COL_SIZE):
            digit = []

            for string in rows:
                digit.append(string[c_idx:c_idx+COL_SIZE])

            cols.append("".join(digit))

        cols = [numbers.get(d, "?") for d in cols]
        cols = "".join(cols)
        digits.append(cols)

    return ",".join(digits)
