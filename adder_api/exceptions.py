
class IncorrectInputException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 61

class IncorrectInputTypeException(IncorrectInputException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 62

class IncorrectInputLengthException(IncorrectInputException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = 63
