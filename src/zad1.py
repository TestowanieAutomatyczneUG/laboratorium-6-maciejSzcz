class FizzBuzz:
    def game(self, num):
        """Takes integer and produces the result based on divisibility of the number
        >>> c = FizzBuzz()
        >>> c.game(5)
        'Buzz'
        >>> c.game(3)
        'Fizz'
        >>> c.game(15)
        'FizzBuzz'
        >>> c.game("12")
        Traceback (most recent call last):
            File "/usr/lib/python3.8/doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.FizzBuzz.game[4]>", line 1, in <module>
                c.game("12")
            File "zad1.py", line 15, in game
                raise Exception("Not a valid number")
        Exception: Not a valid number
        >>> c.game(2)
        Traceback (most recent call last):
            File "/usr/lib/python3.8/doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.FizzBuzz.game[5]>", line 1, in <module>
                c.game(2)
            File "zad1.py", line 32, in game
                raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        """
        if type(num) != int:
            raise Exception("Not a valid number")
        if ((num % 15) == 0):
            return "FizzBuzz"
        elif ((num % 3) == 0):
            return "Fizz"
        elif ((num % 5) == 0):
            return "Buzz"
        else:
            raise Exception("Error in FizzBuzz")

if __name__ == "__main__":
    import doctest
    doctest.testmod()