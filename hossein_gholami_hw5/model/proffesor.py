from person import Person

class Proffesor(Person):
    def __init__(self, name, family, proffesor_id):
        super().__init__(name, family)
        self.proffesor_id = proffesor_id
        self.lecture = []
