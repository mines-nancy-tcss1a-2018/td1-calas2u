# -*- coding:latin-1 -*-
def sommedigit(n):
    somme=0
    for chiffre in str(n):
        somme+=int(chiffre)
    return somme

assert sommedigit(2**15)==26

print ('La somme des digits de 2**1000 est :',sommedigit(2**1000))
