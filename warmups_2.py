

class Person(object):
    school = "ABC Primary School"

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    career = "studying"


class Employee(Person):
    career = "teaching"

john = Employee("John", 23)
peter = Student("Peter", 9)

for person in john, peter:
    print "My name is %s I am %s years old. I am %s at %s" % (person.name, person.age, person.career, person.school)