import unittest
import doctest
import re
import string

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
      File "/usr/lib/python3.8/doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.ValidPassword[6]>", line 1, in <module>
        p.validate(123)
      File "zad2.py", line 24, in validate
        raise TypeError()
    TypeError
    """
    def validate(self, password):
        if type(password) != str:
            raise TypeError()
        elif len(password) < 8:
            return False
        elif re.search('[0-9]', password) is None:
            return False
        elif re.search('[A-Z]', password) is None:
            return False
        elif re.search(f'[{string.punctuation}]', password) is None:
            return False
        else:
            return True

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
        self.assertEqual(self.temp.validate('tojestnowefdfdhasl1o!#'), False)

    def test_password_input_not_string(self):
        self.assertRaises(TypeError, self.temp.validate, 123454325)

    def tearDown(self):
        self.temp = None 

if __name__ == '__main__': # pragma: no cover
    doctest.testmod(extraglobs={'p': ValidPassword()})
    #unittest.main()