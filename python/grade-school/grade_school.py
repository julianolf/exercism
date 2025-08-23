class School(object):
    def __init__(self):
        self._grades = dict()

    def add_student(self, name, grade):
        if grade not in self._grades:
            self._grades[grade] = set()
        self._grades[grade].add(name)

    def roster(self):
        r = []
        for _, v in sorted(self._grades.items()):
            r += sorted(v)
        return r

    def grade(self, grade_number):
        return sorted(self._grades.get(grade_number, []))
