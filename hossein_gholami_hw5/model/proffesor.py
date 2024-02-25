from hossein_gholami_hw5.src.load_proffesor import load_proffesor
from hossein_gholami_hw5.model.person import Person
from hossein_gholami_hw5.src.pick_lecture import pick_lecture
from hossein_gholami_hw5.src.load_proffesor import load_proffesor
from hossein_gholami_hw5.src.write import write_file
import json

class Proffesor(Person):
    def __init__(self, proffesor_id):
        proffesors = load_proffesor()
        proffesor = proffesors[proffesor_id]
        self.name = proffesor['name']
        self.family = proffesor['family']
        super().__init__(self.name, self.family)
        self.proffesor_id = proffesor_id
        self.lecture = proffesor['grade']
        self.status = True


    def pick_lecture(self):
        list_lecture = pick_lecture()
        for key, value in list_lecture.items():
                self.lecture[key] =  value

    def check_status(self):
        if len(self.lecture) >= 3:
            self.status = False
        

    def update(self):
        proffesor = load_proffesor()
        proffesor[self.proffesor_id]['grade'] = self.lecture

        write_file(file_name='/hossein_gholami_hw5/data/proffesor.json', file=json.dumps(proffesor))
