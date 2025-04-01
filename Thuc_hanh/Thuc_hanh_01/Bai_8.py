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

class Student(Person):
    def __init__(self, name:str, yob:int, grade:str):
        self._name = name
        self._yob = yob
        self._grade = grade

    def describe(self):
        print("Student - Name:", self._name, "- YoB:", self._yob, "- grade:", self._grade)

class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        self._name = name
        self._yob = yob
        self._subject = subject

    def describe(self):
        print("Teacher - Name:", self._name, "- YoB:", self._yob, "- subject:", self._subject)

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist:str):
        self._name = name
        self._yob = yob
        self._specialist = specialist

    def describe(self):
        print("Doctor - Name:", self._name, "- YoB:", self._yob, "- specialist:", self._specialist)

class Ward:
    def __init__(self, name:str):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person:Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        ### Your Code Here
        count = 0
        for person in self.__listPeople:
            if isinstance(person, Doctor):
                count += 1
        return count
        ### End Code Here

student1 = Student(name = "studentA", yob = 2010, grade = "7")
teacher1 = Teacher(name = "teacherA", yob = 1969, subject = "Math")
teacher2 = Teacher(name = "teacherB", yob = 1995, subject = "History")
doctor1 = Doctor(name = "doctorA", yob = 1945, specialist = "Endocrinologists")
ward1 = Ward(name = "Ward1")
doctor2 = Doctor(name = "doctorB", yob = 1975, specialist = "Cardiologists")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
assert ward1.count_doctor() == 1
ward1.add_person(doctor2)
print(ward1.count_doctor())