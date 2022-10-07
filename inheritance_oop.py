class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hello i am", self.name, "my age is", self.age, 'Years')

    def talk(self):
        print("Bark!")


class Cat(Dog):
    def __int__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Hello i am", self.name, "my age is", self.age, 'Years')

    def talk(self):
        print("Meow!")


man = Cat('Ron', 19)
man.speak()
man.talk()
