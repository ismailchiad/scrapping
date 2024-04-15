import requests
from bs4 import BeautifulSoup
import json

url="https://catalog.data.gov/dataset"

response = requests.get(url)
# print(response)
content = response.content
# print(content)

# soup : c'est tout le code hmtl
soup=BeautifulSoup(content, 'html.parser')

# Trouver la balise img
image_tags = soup.find_all('img')
# print(image_tags)

# Obtenir l'URL de l'image
# image_url = img["src"]

# print("URL de l'image :", image_url)

# Obtenir les URLs de toutes les images
image_urls = [img["src"] for img in image_tags]

# Afficher les URLs des images
# for url in image_urls:
    #   print("URL de l'image :", url)

# Créer un dictionnaire avec les URLs des images
image_data = {"image_urls": image_urls}

# Convertir le dictionnaire en format JSON
image_json = json.dumps(image_data)
print(image_json)

# cas de la balise html
# balise_header = soup.find("html")
# print(balise_header)

# balise_class = balise_header.get("class")
# print(balise_class)

output_file = "image_json.json"

with open(output_file, "w") as json_file:
    for line in json.dumps(image_json, indent=4).split("\n"):
        json_file.write(line + "\n")

print(output_file)