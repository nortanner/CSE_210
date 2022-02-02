class Student:

    def __init__(self, first_name="",last_name=""):
        self._first_name = first_name
        self._last_name = last_name
        self.__first_name()
        self.__last_name()

    def __first_name(self):
        print(self._first_name)

    def __last_name(self):
        print(self._last_name)

first = input("What is your first name? ").capitalize()
last = input("What is your last name? ").capitalize()

x = Student(first, last)


