def legal(a):
    remain = a
    divider = [7,11,13]
    while(remain>1):
        i=0
        for d in divider:
            if(remain%d==0):
                i+=1
                remain = remain/d
        if(remain==1):
            return True
        elif(i==0):
            return False

def nextNum(a):
    a+=2
    while(not(legal(a))):
        a+=2
    return a

def primeTime(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return nextNum(primeTime(n-1))
a=1
for i in range(200):
    a = nextNum(a)
    print (str(a)+" No"+str(i))
