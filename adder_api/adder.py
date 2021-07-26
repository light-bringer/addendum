from logging import log
import sys
from adder_api.exceptions import (IncorrectInputLengthException, IncorrectInputTypeException, IncorrectInputException)

from adder_api import Log

def parse_command_line_arguements():
    Log.debug("inside Parse command line arguements!")
    args = sys.argv
    filename = args[0]
    cmd_args = args[1:]
    Log.debug("exits Parse command line arguements!")
    Log.debug("{}: {}".format(filename, cmd_args))
    return {
        'file': filename,
        'cmdargs': cmd_args
    }


def validate(array, json=None):
    Log.debug("inside validate")
    try:
        if len(array) != 3:
            Log.warning("length is not equal to 3")
            raise IncorrectInputLengthException()
        else:
            if json:
                Log.info("JSON type")
                for elem in array:
                    if type(elem) != type(1):
                        raise IncorrectInputTypeException()
            array = list(map(int, array))
            return array
    except ValueError:
        Log.warning("ValueError: Incorrect Type Exceptions")
        raise IncorrectInputTypeException()


def array_sum(array):
    Log.debug("inside Array Sum")
    teens = set(i for i in range(13, 20))
    Log.info("teens : {}".format(teens))
    total_sum = 0
    for elem in array:
        if elem in teens:
            pass
        else:
            total_sum += elem

    Log.info("Sum: {}".format(total_sum))
    return total_sum


def cmd():
    Log.debug("command line parser")
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

