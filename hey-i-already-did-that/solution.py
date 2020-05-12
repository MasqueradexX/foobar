def toStr(n,base):
    #Copied from somewhere else :)
    convertString = "0123456789"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

def listToString(s):     
    #Copied from somewhere else :)
    str1 = ""     
    for ele in s:  
        str1 += ele      
    return str1 

def computeZ(n,b):
    x = int(listToString(sorted(n,reverse=True)),base=b)
    y = int(listToString(sorted(n)),base=b)
    z = x - y
    return z


def solution(n, b):
    #Your code here
    k = len(n)
    currentIndex = 0
    prev = dict()
    while True:
        z = computeZ(n,b)
        if z == 0:
            return 1
        n = toStr(z,b).zfill(k)
        if n in prev:
            return currentIndex - prev[n]
        else:
            prev[n] = currentIndex
            currentIndex += 1


print(solution('210022', 3))