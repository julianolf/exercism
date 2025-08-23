class Matrix(object):
    def __init__(self, matrix_string):
        self.data = [
            list(map(int, r.split())) for r in matrix_string.splitlines()
        ]

    def row(self, index):
        return self.data[index - 1]

    def column(self, index):
        return [r[index - 1] for r in self.data]
