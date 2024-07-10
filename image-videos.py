import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime

def download_media(url):
    # Obtener el contenido HTML de la página
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Determinar si existe el selector 'main'
    main_exists = soup.find('main') is not None

    # Seleccionar el contenedor apropiado para las imágenes y los videos
    container = soup.main if main_exists else soup.body

    # Crear un directorio para almacenar las imágenes y los videos
    folder_name = url.replace('/', '_').replace(':', '').replace('.', '_') + '_' + datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(folder_name, exist_ok=True)

    # Encontrar todas las etiquetas de imagen y video dentro del contenedor seleccionado
    media_tags = container.find_all(['img', 'video'])

    # Descargar cada imagen o video encontrados
    for media_tag in media_tags:
        if media_tag.name == 'img':
            media_url = media_tag.get('src')
        elif media_tag.name == 'video':
            media_url = media_tag.find('source').get('src')
        if media_url:
            # Construir la URL completa si es relativa
            media_url = urljoin(url, media_url)
            # Obtener solo el nombre del archivo de la URL
            media_name = os.path.basename(urlparse(media_url).path)
            # Descargar la imagen o video y guardarla en el directorio correspondiente
            with open(os.path.join(folder_name, media_name), 'wb') as f:
                media_response = requests.get(media_url)
                f.write(media_response.content)
                print(f"Media descargado: {media_name}")

# URL de la página web
url = input("Introduce la URL de la página web: ")

# Llamar a la función para descargar imágenes y videos
download_media(url)
