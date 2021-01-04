def nextnum(a):
    a+=1
    while(not(('7' in str(a))^('5' in str(a)))):
        a+=1
    return a

def fiveseven(n):
    if(n <= 0):
        return 0
    elif(n == 1):
        return 5
    else:
        return nextnum(fiveseven(n-1))

print(fiveseven(1000))
