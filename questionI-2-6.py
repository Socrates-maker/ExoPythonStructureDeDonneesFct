

#fonction principale du programme
def main():
    #Declaration de la liste
    A=[14,7,6,12,2,3,3,10]
    tmp = A.copy() #sauvegarde de A
    #Affichache de la liste
    print(A)

    

    #Calcule de la somme des elements de la liste avec la fonction somme
    print('\nSomme des elements de la liste :\n',somme(tmp))

    #Calcule de la moyenne
    print('\nMoyenne des elements de la liste :',moyenne(tmp))

    #Maximum d'une liste
    print('\nLe maximum de la liste est: ',maximum(tmp))

    #Indice du maximum
    print('\nLe maximum de la liste est: ',maximum_indice(tmp))

    #Rechercher un element dans la liste
    x=float(input('Entrer un element a rechercher dans la liste\n'))
    if (recherche(x,tmp)):
        print("Trouvé")
    else:
        print("Non Trouvé")




#Fonction calculant la somme des elements d'une liste de nombres reels
def somme(A):
    s=0
    for i in range(len(A)):
        s = s + A[i]
    return s

#Fonction calculant la moyenne des elements d'une liste
def moyenne(A):
    return somme(A) / len(A)

#Fonction qui calcule le maximum des elements d'une liste
def maximum(A):
    max = 0
    for i in range(len(A)):
        if (A[i]>max):
            max = A[i]
    return max

#Fonction qui renvoie l'indice du maximum
def maximum_indice(A):
    max = 0
    for i in range(len(A)):
        if (A[i]>max):
            max = A[i]
            indce=i
    return indce

#Fonction qui recherche un element dans une liste. renvoie True si l'element
#est trouve et false sinon
def recherche(x,L):
    trouve = False
    for i in range(len(L)):
        if (L[i]==x):
            trouve=True 
    if (trouve):
        return True
    else:
        return False



if __name__=="__main__":
    main()
