"""Handles all of the necessary preparatory work. Can be thought of as a module for general utilities as well."""


import requests


# General

def get_anilist_genres() -> list:
    """Queries the AniList API and returns a list of all of the genres.

    Returns:
        genres (list): A list of all of the genres on AniList.
    """
    query = '''
        query {
            GenreCollection
        }
    '''
    genres = requests.post(query_url, json={'query': query}).json()
    genres = genres['data']['GenreCollection']

    return genres


def get_list_lowercase(array: list[str]) -> list[str]:
    """Takes in a list of strings and returns that same list, with every string being lowercase.

    Args:
        array (list[str]): The list of strings.

    Returns:
        list[str]: The same list of strings, but with every string being lowercase.
    """

    return list(map(str.lower, array))


query_url = 'https://graphql.anilist.co'
anilist_genres = get_anilist_genres()


def main():
    pass


if __name__ == '__main__':
    main()
