from person import Person


class Student(Person):
    def __init__(self, name, family, student_id):
        super.__init__(name, family)
        self.student_id = student_id
        self.status = 0
        self.grade = []

