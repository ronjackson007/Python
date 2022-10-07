def hillvalley(l):
    if (len(l) < 3):
        return False

    up_count = 1
    low_count = 1

    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            if low_count > 1:
                return False
            up_count = up_count + 1
        if l[i] < l[i + 1]:
            low_count = low_count + 1
        if l[i] == l[i + 1]:
            return False

    if up_count > 1 and low_count > 1:
        return True
    else:
        return False



print(hillvalley([1,2,3,4,5,3,2,4,5,3,2,1]))
print(hillvalley([1,2,3,5,4]))