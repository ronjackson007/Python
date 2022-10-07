# map function
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func(x): return x ** x


# Common method
new_list = []
for x in li:
    new_list.append(func(x))

print(new_list)

# Map function gives same output
print(list(map(func, li)))

# list comprehension
print([func(x) for x in li])
# only for even
print([func(x) for x in li if x % 2 == 0])

