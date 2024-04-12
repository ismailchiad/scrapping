# écrire une fonction qui a comme paramètre une liste et un element d'une liste
# qui retourne la position de cet élément dans la liste

#cas 1 : sans boucle
def index_liste (liste, elem):
    position = liste.index(elem)
    return position

liste = [1, 2, 45, 9, 38, 41, 64]
elem = 45
position = index_liste(liste, elem)

print (position)

#cas 2 : avec boucle
def index_liste_boucle (liste, elem):
    position = -1
    for i in liste:
        if i == elem: 
            return position
        position += 1

ma_liste = [1, 2, 45, 9, 9, 38, 41, 64]
mon_elem = 9

position_boucle = index_liste_boucle(ma_liste,mon_elem)
print(position_boucle)

#cas 3 : méthode amadou
def position(list, elt):
    result = -1
    #for element in list:
        #print(element)
        #if list[i] != "":
        #    return(i)
        #else:
        #    print("L'element" + list[i] + "n'existe pas dans la liste")
    for i in range(len(list)):
        if list[i] == elt:
           # print(list[i])
            result = i
        else:
            print("l'element n'a pas été trouvé")
    return result

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
result = position(list, 3)
print(result)

# #fonction qui prends en paramètre une liste et qui inverse tous les élèments de cette liste
# def inverse_liste(liste):
#     return liste[::-1]

# liste = [1, 2, 3, 4, 5, 6]
# liste_inverse = inverse_liste(liste)
# print (liste)
# print(liste_inverse)

# def inverse_liste_2(list):
#     return list(reversed(list))

# ma_liste = [1, 2, 3, 4, 5]
# liste_inverse = inverse_liste_2(ma_liste)
# print(ma_liste)
# print(liste_inverse)

#meme exercice avec boucle for
def liste_inverse(liste):
    liste_inverse = []
    for i in range(len(liste)):
        element = liste.pop()
        liste_inverse.append(element)
    return liste_inverse

ma_liste = [1, 2, 3, 4, 5, 9]
liste_inverse = liste_inverse(ma_liste)
print(ma_liste)
print(liste_inverse)

# from faker import Faker

# # Créer une instance de Faker
# fake = Faker()

# # Générer des données de noms, prénoms et adresses e-mail
# for _ in range(5):
#     nom = fake.last_name()
#     prenom = fake.first_name()
#     email = fake.email()
#     print(f"Nom: {nom}, Prénom: {prenom}, Email: {email}")

# méthode while
def reverseOrdre(list):
    inv = []
    i = len(list)-1
    while i >= 0:
        inv.append(list[i])
        i -= 1
    return inv

list = [1, 2, 3, 4, 5]
list_invert = reverseOrdre(list)
print(list_invert)