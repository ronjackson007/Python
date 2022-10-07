from distutils.archive_util import make_archive


class Car(object):
    def __init__(self, make, model, year, condition="New", kms="0"):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    
    def display(self, showAll=True):
        if showAll:  # by default the value is true similar to -->> showAll == True
            print("This car is a %s %s from %s, It is %s and has %s kms run." % (self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is %s %s from %s." % (self.make, self.model, self.year))

# res = car('Ferari', 'Narxi', 2020, 'New', 0)


res = Car('Ferari', 'Narxi', 2020)
res.display()
