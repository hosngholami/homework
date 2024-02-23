class StatusGradeError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "can not take grade becuse you'r avg lower 12"
        super().__init__(self.message)