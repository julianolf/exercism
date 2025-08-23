class Garden(object):
    PLANTS = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets'
    }

    STUDENTS = (
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    )

    def __init__(self, diagram='', students=STUDENTS):
        self.diagram = diagram.split()
        self.students = sorted(students)

    def plants(self, student):
        if len(self.diagram) != 2:
            raise ValueError('Invalid diagram')
        if student not in self.students:
            raise ValueError('Invalid student')

        row1, row2 = self.diagram
        idx = self.students.index(student) * 2
        vegs = list(row1[idx:idx+2]) + list(row2[idx:idx+2])

        return [self.PLANTS[v] for v in vegs]
