
def mys(m):
    if m == 1:
        return 1
    else:
        return m * mys(m-1)


res = mys(5)
print(res)
