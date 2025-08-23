from collections import defaultdict


class School(object):
    def __init__(self):
        self._grades = defaultdict(set)

    def add_student(self, name, grade):
        self._grades[grade].add(name)

    def roster(self):
        r = []
        for _, v in sorted(self._grades.items()):
            r += sorted(v)
        return r

    def grade(self, grade_number):
        return sorted(self._grades.get(grade_number, []))
