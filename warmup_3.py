__author__ = 'macuser'

class Job(object):
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary



class Employee(object):
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.job = Job(position, salary)

john = Employee("John", 24, "Software Developer", 60000)

print "My name is %s, I am %s years old and I am a %s" % (john.name, john.age, john.job.position)
