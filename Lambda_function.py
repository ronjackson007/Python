# Lambda Function
def func1(x):
    return x + 6


func2 = lambda x: x + 6


def func3(x):
    func4 = lambda x: x + 6
    return func4(x) + x + 6


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(func1(3))
print(func2(5))
print(func3(4))
print(list(map(lambda x: x ** x, li)))
print(list(map(lambda x: x % 2 == 0, li)))
print(list(filter(lambda x: x % 2 == 0, li)))

