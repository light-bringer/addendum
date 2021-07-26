import sys
from adder_api.exceptions import *

def parse_command_line_arguements():
    args = sys.argv
    filename = args[0]
    cmd_args = args[1:]
    return {
        'file': filename,
        'cmdargs': cmd_args
    }


def validate(array):
    try:
        if len(array) != 3:
            raise IncorrectInputLengthException()
        else:
            array = list(map(int, array))
            return array
    except ValueError:
        raise IncorrectInputTypeException()


def array_sum(array):
    teens = set(i for i in range(13, 20))
    total_sum = 0
    for elem in array:
        if elem in teens:
            pass
        else:
            total_sum += elem
    
    return total_sum


def cmd():
    arguments = parse_command_line_arguements()
    cmd_args = arguments['cmdargs']
    try:
        num_array = validate(cmd_args)
        print(array_sum(num_array))
        return
    except IncorrectInputLengthException:
        print("Exactly 3 numbers are required")
        return
    except IncorrectInputTypeException:
        print("All inputs must be numeric")
        return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmd()

