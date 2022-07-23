

#fonction principale du programme
def main():
    #Declaration de la liste
    A=[14,7,6,12,2,3,3,10]
    tmp = A.copy() #sauvegarde de A
    #Affichache de la liste
    print(A)

    #Division du dernier element de la list par 2
    A[-1]=int(A[-1]/2)
    print(A)

    #Retrancher 1 a tous les elements de la liste
    for i in range(len(A)):
        A[i]=A[i] - 1
    print(A)

    #Affichage de tous les elements de la liste sur differentes lignes
    print("\nAffichage des elements de la liste sur differentes lignes")
    for i in range(len(A)):
        print(A[i])

    #Faire afficher seulement les nombres pairs
    print("\nNombres pairs de la liste")
    for i in range(len(A)):
        if(A[i]%2==0):
            print(A[i])

    #Faire afficher 10 fois chaque element de la liste sur une lignes
    print("\nFaire afficher 10 fois chaque element de la liste sur une lignes")
    for i in range(len(A)):
        for j in range(10):
            print(A[i],end=' ')
        print('')

    #Afficher chaque element autant de fois que sa valeur
    print("\nAfficher un element autant de fois que sa valeur")
    for i in range(len(A)):
            for j in range(A[i]):
                print(A[i],end=' ')
            print('')

    #Calcule de la somme des elements de la liste avec la fonction somme
    print('\n Somme des elements de la liste d\'origine:\n',somme(tmp))

    #Calcule de la moyenne
    print('\n Moyenne des elements de la lste d\'origine :',moyenne(tmp))




#Fonction calculant la somme des elements d'une liste de nombres reels
def somme(A):
    s=0
    for i in range(len(A)):
        s = s + A[i]
    return s

#Fonction calculant la moyenne des elements d'une liste
def moyenne(A):
    return somme(A) / len(A)




if __name__=="__main__":
    main()
