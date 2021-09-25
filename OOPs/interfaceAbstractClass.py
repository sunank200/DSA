from abc import ABCMeta, abstractstaticmethod


# python doesn't have a way to interface explicitly so add 'I' to class name.
class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """
        Interface method
        :return:
        """


class Student(IPerson):
    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("I am a student.")


class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic teacher name."

    def person_method(self):
        print("I am a teacher.")


if __name__ == "__main__":
    s1 = Student()
    s1.person_method()

    t1 = Teacher()
    t1.person_method()
