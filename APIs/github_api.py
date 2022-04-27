import requests


def buscar_avatar(usuario):
    """
    Busca i avatar de um usuário no Github


    :param usuario: str com o nome de usuario no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    answer = requests.get(url)
    return answer.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('pedrocanizel'))
