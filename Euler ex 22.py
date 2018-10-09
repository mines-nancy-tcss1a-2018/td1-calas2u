# -*- coding:latin-1 -*-


with open("p022_names.txt", 'r') as fich:
    texte=fich.read()
    texte=texte.split("\",\"")
    texte[0]=texte[0].lstrip("\"")
    texte[-1]=texte[-1].rstrip("\"")
    texte.sort()
    print (texte)

def Names_score(liste):
    score=0
    alphaB="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for nom in liste:
        score_nom=0
        for lettre in nom:
            k=0
            while lettre!=alphaB[k] and k<=50:
                k+=1
            score_nom+=k+1
        score+=score_nom*(liste.index(nom)+1)
    return score

assert Names_score(["ABB","CA"])==5*1+4*2

print ("Le score est de :",Names_score(texte))


        
        