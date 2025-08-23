class Matrix(object):
    def __init__(self, matrix_string):
        self.data = [list(map(int, r.split()))
                     for r in matrix_string.split('\n')]

    def row(self, index):
        return self.data[index]

    def column(self, index):
        return [r[index] for r in self.data]
