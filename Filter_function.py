# filter function
def is_odd(x):
    return x % 2 != 0


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(is_odd, li)))
print(list(map(is_odd, li)))
print(list(map(is_odd, filter(is_odd, li))))
