import requests
from bs4 import BeautifulSoup

url="https://catalog.data.gov/dataset"

response = requests.get(url)
# print(response)
content = response.content
# print(content)

# soup : c'est tout le code hmtl
soup=BeautifulSoup(content, 'html.parser')

# Trouver la balise img
# image_tags = soup.find_all('img')
# print(image_tags)

# Obtenir l'URL de l'image
# image_url = img["src"]

# print("URL de l'image :", image_url)

# Obtenir les URLs de toutes les images
# image_urls = [img["src"] for img in image_tags]

# Afficher les URLs des images
# for url in image_urls:
#     print("URL de l'image :", url)

# cas de la balise span
balise_span = soup.find('span')
print(balise_span)