from re import L


# table = int(input("Enter the number you want the factorial of \n"))
num = 5
fac = 1
# print("\n")

for i in range(1, num + 1):
    fac *= i
print(fac)
