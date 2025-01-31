import requests

def get_commit_count_by_author(repo_url, username):
    try:
        # Extrae el propietario y el nombre del repositorio de la URL
        parts = repo_url.rstrip('/').split('/')
        owner = parts[-2]
        repo = parts[-1]
        
        # URL de la API de GitHub para obtener los commits
        api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        
        # Parámetros de la solicitud
        params = {'author': username}
        
        # Inicializamos una lista para los commits y la página
        commits = []
        page = 1

        while True:
            # Agregamos el parámetro de paginación
            params['page'] = page
            response = requests.get(api_url, params=params)
            response.raise_for_status()

            # Parseamos los commits
            commits_page = response.json()
            commits.extend(commits_page)

            # Si no hay más commits, salimos del bucle
            if len(commits_page) == 0:
                break
            
            # Incrementamos la página
            page += 1

        # Devuelve la cantidad total de commits
        return len(commits)
    except Exception as e:
        print(f"Error: {e}")
        return 0

# URL del repositorio en GitHub
repo_url = 'https://github.com/Jordan-Iralde'

# Nombre del usuario cuyos commits quieres contar
username = 'Jordan%20Iralde'  # Reemplaza los espacios por '%20'

# Muestra la cantidad de commits del usuario
commit_count = get_commit_count_by_author(repo_url, username)
print(f"El usuario {username} tiene {commit_count} commits en el repositorio {repo_url}.")
