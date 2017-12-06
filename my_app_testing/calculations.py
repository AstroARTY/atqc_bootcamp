def fyb(n):
    if n==0:
        l=[]
    elif n==1:
        l=[0]
    elif n<0:
        print('Negative values are not allowed')
    else:
        l=[0,1]
        for i in range(2,n):
            a=l[i-1] + l[i-2]
            l.append(a)
    print(l)


def pairs(n):
    for i in range(len(n)-1):
        if n[i] + n[i+1] == 10:
            print(n[i], n[i+1])
