class Calc(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_calc(self):
        print("The sum of these two numbers are", self.num1+self.num2)


num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

num = Calc(num1, num2)
num.add_calc()
