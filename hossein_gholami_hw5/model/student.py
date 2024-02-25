from hossein_gholami_hw5.model.person  import Person
from hossein_gholami_hw5.src.load_student import load_student
from hossein_gholami_hw5.src.pick_lecture import pick_lecture
from hossein_gholami_hw5.src.write import write_file
from hossein_gholami_hw5.src.grade_lecture import grade_lecture
import json
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
        try:
            sum = 0
            count = 0
            for key, value in self.grade.items():
                if value != '-1':
                    sum += float(value)
                    count += 1
            if (sum / count) < 12:
                self.status = False
        except ZeroDivisionError as ze:
            self.status = True
        except AttributeError as ab:
            print('plase take lecture')
            
      
    def update(self):
        student = load_student()
        student[self.student_id]['grade'] = self.grade


        write_file(file_name='/hossein_gholami_hw5/data/student.json', file=json.dumps(student))


    def pick_lecture(self):
         list_lecture = pick_lecture()
         list_lecture = grade_lecture(list_lecture)
         for key, value in list_lecture.items():
                self.grade[key] =  value


        

    # def __repr__(self) -> str:
    #     return f'{self.student_id} give {self.grade}'


