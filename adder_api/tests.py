from adder_api import exceptions, adder
from logging import exception
import unittest


class TestAdderMethods(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(adder.array_sum([1, 2, 3]), 6)
    
    def test_addition_teen(self):
        self.assertEqual(adder.array_sum([1, 15, 1]), 2)

    def test_length_nothrow_exceptions(self):
        try:
            adder.validate([1, 2, 3])
        except exceptions.IncorrectInputLengthException:
            self.fail("validate() raised IncorrectInputLengthException unexpectedly!")
        except exceptions.IncorrectInputTypeException:
            self.fail("validate() raised IncorrectInputTypeException unexpectedly!")
    
    def test_length_exception_lt3(self):
         with self.assertRaises(exceptions.IncorrectInputLengthException) as cm:
            data = adder.validate([4, 5])
            print(data, cm)
            the_exception = cm.exception
            self.assertEqual(the_exception, None)


    def test_length_exception_gt3(self):
        with self.assertRaises(exceptions.IncorrectInputLengthException) as cm:
            data = adder.validate([1, 2, 3, 4, 5])
            print(data, cm)
            the_exception = cm.exception
            self.assertEqual(the_exception, None)
    
    def test_content_type_exception(self):
        with self.assertRaises(exceptions.IncorrectInputTypeException) as cm:
            data = adder.validate([4, 5, 'a'])
            print(data, cm)
            the_exception = cm.exception
            self.assertEqual(the_exception.error_code, 63)


    def test_length_content_exception(self):
         with self.assertRaises((exceptions.IncorrectInputTypeException, exceptions.IncorrectInputLengthException)) as cm:
            data = adder.validate([1, 2, 3, 4, 5])
            print(data, cm)
            the_exception = cm.exception
            self.assertSetEqual({61, 62, 63}, the_exception.error_code)


if __name__ == '__main__':
    unittest.main()