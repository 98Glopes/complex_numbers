import unittest
from complex_number import ComplexNumber

class VerifyComplexNumberOperations(unittest.TestCase):

    def test_add_method(self):

        a = ComplexNumber('rec', 2, 2)
        b = ComplexNumber('rec', 2, 2)

        result = a + b
        expected_result = ComplexNumber('rec', 4, 4)

        self.assertEqual(expected_result.real, result.real)
        self.assertEqual(expected_result.imag, result.imag)

        
    def test_sub_method(self):

        a = ComplexNumber('rec', 4, 2)
        b = ComplexNumber('rec', 2, 2)

        result = a - b
        expected_result = ComplexNumber('rec', 2, 0)

        self.assertEqual(expected_result.real, result.real)
        self.assertEqual(expected_result.imag, result.imag)
