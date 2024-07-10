import instaloader
#pip install instaloader

def download_instagram_images(username):
    # Crear una instancia de Instaloader
    loader = instaloader.Instaloader()

    # Descargar el perfil de Instagram
    try:
        loader.download_profile(username, profile_pic_only=False)
        print(f"Descarga completa para el perfil: {username}")
    except Exception as e:
        print(f"Error al descargar el perfil: {username}")
        print(e)

if __name__ == "__main__":
    # Reemplaza 'username' con el nombre de usuario del perfil que quieres descargar
    username = "nombre_de_usuario"
    download_instagram_images(username)