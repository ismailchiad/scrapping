import requests
from bs4 import BeautifulSoup


def extraire_titres_principaux(url, nom_fichier):
    response = requests.get(url)
    content = response.content

    soup=BeautifulSoup(content, 'html.parser')

    grand_titres = soup.find("div", id="mw-content-text").find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

    # sort par ordre alphabétique
    # grand_titres.sort(key=lambda x: x.text.strip())

    # Créer une chaîne de caractères pour stocker les titres
    titres_texte = ""
    for titre in grand_titres:
        titres_texte += titre.text.strip() + "\n"
    
    # Écrire les titres dans un fichier texte
    with open(nom_fichier, "w") as fichier:
        fichier.write(titres_texte)

url_saisie = "https://fr.wikipedia.org/wiki/France"
nom_fichier_sortie = "titres_principaux.txt"
titres_principaux = extraire_titres_principaux(url_saisie,nom_fichier_sortie)

url_saisie2 = "https://fr.wikipedia.org/wiki/Maroc"
nom_fichier_sortie = "titres_principaux2.txt"
titres_principaux2 = extraire_titres_principaux(url_saisie2,nom_fichier_sortie)
