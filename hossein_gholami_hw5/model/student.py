from hossein_gholami_hw5.model.person  import Person
from hossein_gholami_hw5.src.load_student import load_student

class Student(Person):
    def __init__(self, student_id):

        try:
            student = load_student()
            student = student[student_id]
            self.name = student['name']
            self.family = student['family']
            super().__init__(self.name, self.family)
            self.student_id = student_id
            self.status = True
            self.grade = student['grade']
        except KeyError as ke:
            print('key not found')
        except TypeError as te:
            print(te)

        


    def check_status(self):
        sum = 0
        count = len(self.grade)
        for item in self.grade:
            sum += self.grade[item]
        if (sum / count) < 12:
            self.status = False
            print(self.status)
            

    def __repr__(self) -> str:
        return f'{self.student_id} give {self.grade}'


