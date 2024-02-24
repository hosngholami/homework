class GradeError(Exception):
    def __init__(self, message, grade):
        self.message = message
        self.grade = grade
        super().__init__(self.message)


    def __repr__(self):
        return f'{self.grade} most between 1 to 20'