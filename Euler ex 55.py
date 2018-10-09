# -*- coding:latin-1 -*-

def retourne(n):
    nbr=""
    for i in str(n):
        nbr=i+nbr
    return int(nbr)

assert retourne(157)==751
assert retourne(9)==9

def lychrel(nbr):
    k=0
    nbr=nbr+retourne(nbr)
    while retourne(nbr)!=nbr and k<=50:
        nbr=nbr+retourne(nbr)
        k+=1
    if retourne(nbr)==nbr:
        return False
    return True

assert lychrel(47)==False

def nbr_lychrel(n):
    nbrlychrel=0
    for i in range(1,n+1):
        if lychrel(i):
            nbrlychrel+=1
    return nbrlychrel

assert nbr_lychrel(4)==0

print("Le nombre de nombre Lychrel entre 0 et 10 000 est :",nbr_lychrel(10000))
    
    
