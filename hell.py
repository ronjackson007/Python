class Dog(object):
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def speak(self):
        print("Hello i am", self.name, "my age is", self.age, "and i am from", self.country)


manu = Dog("Ron", 13, "India")
man = Dog("Jack", 34, "US")

manu.speak()
man.speak()
