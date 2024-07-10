import instaloader
#pip install instaloader

def download_latest_posts(username, post_count=5):
    # Crear una instancia de Instaloader
    loader = instaloader.Instaloader()

    # Obtener el perfil de Instagram
    profile = instaloader.Profile.from_username(loader.context, username)

    # Descargar las últimas 5 publicaciones
    posts = profile.get_posts()
    for index, post in enumerate(posts):
        if index < post_count:
            loader.download_post(post, target=f"{username}_post_{index+1}")
        else:
            break

    print(f"Descarga completa para el perfil: {username}")

if __name__ == "__main__":
    # Reemplaza 'nombre_de_usuario' con el nombre de usuario del perfil que quieres descargar
    username = "nombre_de_usuario"
    download_latest_posts(username)