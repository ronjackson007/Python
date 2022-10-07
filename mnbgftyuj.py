def hillvalley(l):
    asc = 0
    des = 0
    point = 0

    for i in range(0, len(l)):
        if (i>0 and i<len(l)-1) and (l[i]>l[i-1] and l[i]<l[i+1]):
            asc += 1
        elif (i>0 and i<len(l)-1) and (l[i]<l[i-1] and l[i]>l[i+1]):
            des += 1
        elif ((i>0 and i<(len(l)-1)) and ((l[i]<l[i-1] and l[i]<l[i+1]) or (l[i]>l[i-1] and l[i]>l[i+1]))):
            point += 1
            if l[i] > l[i+1]:
                des += 1
            elif l[i] < l[i+1]:
                asc += 1
            if l[i] > l[i-1]:
                asc += 1
            elif l[i] < l[i-1]:
                des += 1

        elif (i>0 and i<len(l)-1) and (l[i]==l[i+1] or l[i]==l[i-1]):
            point += 1
        elif (i==0 and l[i]<l[i+1]) or (i==(len(l)-1) and l[i]>l[i-1]):
            asc += 1
        elif (i==0 and l[i]>l[i+1]) or (i==(len(l)-1) and l[i]<l[i-1]):
            des += 1
        else:
            return False

    if asc>=2 and des>=2 and point==1 and len(l)>3:
        return True
    else:
        return False



