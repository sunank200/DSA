"""
https://sourcemaking.com/design_patterns/factory_method
"""
from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method(self):
        """
        Interface for person method.
        :param self:
        :return:
        """


class Student(IPerson):
    def __init__(self):
        self.name = "Student name"

    def person_method(self):
        print("I am a student.")


class Teacher(IPerson):
    def __init__(self):
        self.name = "Teacher name"

    def person_method(self):
        print("I am a teacher.")


class PersonFactoryOption1:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder


class PersonFactoryOption1ServiceProvider(PersonFactoryOption1):
    def get(self, person_id, **kwargs):
        return self.create(person_id, **kwargs)


class PersonFactoryOption2:
    """
    Static methods have a very clear use-case. When we need some functionality
    not w.r.t an Object but w.r.t the complete class, we make a method static.
    This is pretty much advantageous when we need to create Utility methods as
     they aren’t tied to an object lifecycle usually.
    """

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        raise Exception("invalid person type")


if __name__ == "__main__":
    factory = PersonFactoryOption1ServiceProvider()
    factory.register_builder("Student", Student())
    factory.register_builder("Teacher", Teacher())

    config = {}
    s = factory.get("Student", **config)
    s.person_method()

    t = factory.get("Teacher", **config)
    t.person_method()

    choice = input("What type of person do you want to build?")
    person_factory = PersonFactoryOption2.build_person(choice)
    person_factory.person_method()
