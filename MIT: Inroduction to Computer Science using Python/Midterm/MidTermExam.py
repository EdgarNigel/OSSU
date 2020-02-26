## Problem 1 ##

def closest_power(base, num):

    if num == 1:
        return 0
    
    exponent = 0
    
    while base**exponent < num:
        exponent += 1
    
    if abs(num - base**exponent) >= abs(num - base**(exponent-1)):
        return exponent - 1
    else:
        return exponent


## Problem 2 ##

def dotProduct(listA, listB):
    
    result = 0
    
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    
    return result

## Problem 3 ##

def dict_invert(d):
    
    newDict = {}
    
    for k, v in d.items():
        if v not in newDict:
            newDict[v] = [k]
        else:
            newDict[v].append(k)
            newDict[v].sort()
        
    return newDict

## Problem 4 ##

def laceStringsRecur(s1, s2):

    def helpLaceStrings(s1, s2, out):
        
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out+s1[0]+s2[0])
    
    return helpLaceStrings(s1, s2, '')

## Problem 5 ##

def general_poly(L):

    def applyIt(x):
        
        n = 0
        
        for i in L:
            n = x * n + i
        return n
    
    return applyIt