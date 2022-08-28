"""Handles all of the necessary preparatory work. Can be thought of as a module
for general utilities as well."""


import requests


query_url = 'https://graphql.anilist.co'


def get_genres() -> list:
    """Queries the AniList API and returns a list of all of the genres.

    Returns:
        genres (list): A list of all of the genres on AniList.
    """
    query = '''
        query {
            GenreCollection
        }
    '''
    genres = requests.post(query_url,
                           json={'query': query}).json()
    genres = genres['data']['GenreCollection']

    return genres


def main():
    pass


if __name__ == '__main__':
    main()
