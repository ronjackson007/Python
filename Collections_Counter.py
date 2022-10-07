#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):

    if s[:2] == '12' and s[-2:] == 'AM':
        return '00' + str(s[2:-2])
    elif s[-2:] == 'AM':
        return s[:-2]
    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:8]

# Write your code here




result = timeConversion('12:40:45AM')
print(result)


