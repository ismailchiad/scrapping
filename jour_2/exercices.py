# 1. Définir une fonction qui prend en paramètre une liste de nombre et qui renvoie une liste avec les nombres pairs

def nomb_pair(liste):
    liste_pair = []
    for i in liste:
        if i % 2 == 0:
            liste_pair.append(i)
    return liste_pair

ma_liste1 = [1, 2, 3, 4, 5, 9]
liste_pair = nomb_pair(ma_liste1)
print(ma_liste1)
print(liste_pair)

ma_liste2 = [71, 52, 34, 24, 85, 97]
liste_pair2 = nomb_pair(ma_liste2)
print(ma_liste2)
print(liste_pair2)

# Définir une fonction qui fusinne deux listes index par index. Par exemple, [a,b,c] et [1,2,3] devraient devenir [a1,b2,c3].

def fusionne2listes (index1, index2):
    listefusionne = []
    for element1, element2 in zip(index1, index2):
        listefusionne.append(str(element1) + element2)
    return listefusionne

index1 = [1, 2, 3, 4, 5, 9, 11, 54, 87]
index2 = ['a', 'b', 'c', 'd', 'e', 'f']
listefusionne = fusionne2listes(index1, index2)
print(index1)
print(index2)
print(listefusionne)

# Définir une fonction qui élimine les doublons d'une liste sans utiliser la fonction set().

def supprimDoublons (liste):
    listeAdoublons=[]
    for i in liste:
        if i not in listeAdoublons:
            listeAdoublons.append(i)
    return listeAdoublons

liste = ['fiat', 'renault', 'peugeot', 'fiat']
listeAdoublons = supprimDoublons(liste)
print (liste)
print (listeAdoublons)
            

# Définir une fonction qui effectue une rotation à gauche des éléments d'une liste. Par exemple, la liste [1,2,3,4] après une rotation à gauche devient [2,3,4,1].

def rotation_gauche(liste):
    premier_element = liste[0]        # premier_element = 1
    taille = len(liste)               # taille = 3  
    for i in range(taille - 1):
        liste[i] = liste[i + 1]       #   
    liste[taille - 1] = premier_element
    return liste

# Exemple d'utilisation
liste = [1, 2, 3, 4]
rotation_resultat = rotation_gauche(liste)
print("Liste originale :", liste)
print("Liste après rotation à gauche :", rotation_resultat)


