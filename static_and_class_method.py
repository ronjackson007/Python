class People(object):
    population = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def anAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old.')


ask = People('Manu', 19)
print(ask.display())
print(People.anAdult(19))
