from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist:str):
        ### Your Code Here
        self._name = name
        self._yob = yob
        self._specialist = specialist
        ### End Code Here

    def describe(self):
        ### Your Code Here
        print("Doctor - Name:", self._name, "- YoB:", self._yob, "- specialist:", self._specialist)
        ### End Code Here

doctor1 = Doctor(name = "doctorZ2023", yob = 1981, specialist = "Endocrinologists")
assert doctor1._yob == 1981
doctor1.describe()