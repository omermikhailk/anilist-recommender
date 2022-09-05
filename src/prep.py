"""Handles all of the necessary preparatory work. Can be thought of as a module
for general utilities as well."""


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
    genres = requests.post(query_url,
                           json={'query': query}).json()
    genres = genres['data']['GenreCollection']

    return genres


def get_lowercase_genres(genres: list[str]) -> list[str]:
    """Takes in a list of genres and returns that same list, with every
    genre being lowercase.

    Args:
        genres (list[str]): The list of genres.

    Returns:
        list[str]: The same list of genres, with every element being converted
            to be lowercase.
    """
    return list(map(str.lower, genres))


# Arg cleaning

def get_user_genres(genres: list[list[str]]) -> list[str]:
    """Takes in a list of genres, from the command line `--genre` argument
    input, which is a 2D list, and returns the flattened version of it.

    [['slice', 'of', 'life'], ['comedy']] -> ['slice of life', 'comedy']

    Args:
        genres (list[list[str]]): A 2D list of the genres that the user is
            interested in.

    Returns:
        list[str]: The same genres, however in a 1D list.
    """
    return [' '.join(genre) for genre in genres]


query_url = 'https://graphql.anilist.co'
anilist_genres = get_anilist_genres()


def main():
    pass


if __name__ == '__main__':
    main()
