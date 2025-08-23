from itertools import product


def board(input_board):
    if input_board == []:
        return []

    if type(input_board) != list:
        raise ValueError('Invalid input type')

    rows = len(input_board)
    columns = len(input_board[0])
    mines = len(''.join(input_board))
    if mines != (columns * rows):
        raise ValueError('Invalid board size')

    minefield = [[0] * columns for _ in range(rows)]
    for i, j in product(range(rows), range(columns)):
        if input_board[i][j] == '*':
            minefield[i][j] = -10
            neighbours = product((i-1, i, i+1),
                                 (j-1, j, j+1))
            for r, c in neighbours:
                if r < 0 or c < 0:
                    continue
                try:
                    minefield[r][c] += 1
                except IndexError:
                    pass
        elif input_board[i][j] != ' ':
            raise ValueError('Invalid character')

    def _gc(n):
        return ((' ', '*')[n < 0], str(n))[n > 0]

    return [''.join(map(_gc, r)) for r in minefield]
