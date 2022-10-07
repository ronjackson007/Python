#celcius to Fahrenheit c  = ( F - 32 ) * 5/9

def ctof(x):
    x = ( x - 32 ) * (5/9)
    return x

fah = int(input("Enter the Fahrenheit value = "))
print("Your celcius value of ", fah, " is = ", ctof(fah))
