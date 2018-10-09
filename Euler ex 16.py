# -*- coding:latin-1 -*-
def sumdigit(n):
    sum=0
    for e in str(n):
        sum+=int(e)
    return sum

assert sumdigit(2**15)==26

print ('La somme des digits de 2**1000 est :')
print (sumdigit(2**1000))