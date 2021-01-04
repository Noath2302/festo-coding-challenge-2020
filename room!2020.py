import re

pattern = r".*2.*0.*2.*0.*"

# re.match(pattern, numToMatch)

def nextNum(numNow):
    numNow+=1
    while(re.match(pattern, str(numNow))):
        numNow+=1
    return numNow

def roomNum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return nextNum(roomNum(n-1))

num = 0
for i in range(1000000):
    num = nextNum(num)
print(num)
