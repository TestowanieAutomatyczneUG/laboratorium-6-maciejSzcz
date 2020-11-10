import unittest
import doctest

class ValidPassword:
    """
    >>> p = ValidPassword()
    >>> p.validate('ScalaFavL4nguage!')
    True
    >>> p.validate('Pswd1!')
    False
    >>> p.validate('Haslonowee!')
    False
    >>> p.validate('Pswddfsag1')
    False
    >>> p.validate('tojestnowehaslo!#')
    False
    >>> p.validate(123)
    Traceback (most recent call last):
    """
    def validate(self, password):
        return False

class ValidPasswordTest(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()
    
    def test_password_correct_input(self):
        self.assertEqual(self.temp.validate('ScalaFavL4nguage!'), True)

    def test_password_too_short_input(self):
        self.assertEqual(self.temp.validate('Pswd1!'), False)
    
    def test_password_no_digit_in_input(self):
        self.assertEqual(self.temp.validate('Haslonowee!'), False)

    def test_password_no_special_char(self):
        self.assertEqual(self.temp.validate('Pswddfsag1'), False)

    def test_password_no_capital_letter(self):
        self.assertEqual(self.temp.validate('tojestnowehaslo!#'), False)

    def test_password_input_not_string(self):
        self.assertRaises(TypeError, self.temp.validate, 123454325)

    def tearDown(self):
        self.temp = None 

if __name__ == '__main__':
    doctest.testmod(extraglobs={'p': ValidPassword()})