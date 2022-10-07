from distutils.archive_util import make_archive


class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self, showAll='car'):
        if showAll == 'car':  # by default the value is true similar to -->> showAll == True
            print("This car is a %s %s from %s." % (self.make, self.model, self.year))
        elif showAll == 'bike':
            print("This bike is %s %s from %s." % (self.make, self.model, self.year))
        else:
            print("Invalid Input")


# res = car('Ferari', 'Narxi', 2020, 'New', 0)


res = Car('Ferari', 'Narxi', 2020)
res.display('bike')
