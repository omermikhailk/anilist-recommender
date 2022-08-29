"""Handles all of the necessary preparatory work. Can be thought of as a module
for general utilities as well."""


from anime import Anime
from manga import Manga
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


def get_lowercase_genres(genres):
    return list(map(str.lower, genres))


# Arg cleaning

def get_user_genres(genres):
    return [' '.join(genre) for genre in genres]


# List filtering based on args

def sort_score(media_list: list[Anime | Manga]) -> list[Anime | Manga]:
    """Sorts a list of anime or manga, by their scores on AniList, in
    descending order.

    Args:
        media_list (list[Anime | Manga]): A list of anime or manga,
            containing instances of the `Anime` or `Manga` classes.

    Returns:
        sorted_list (list[Anime | Manga]): A sorted list of anime or manga
            entries, in descending order of their scores on AniList.
    """
    sorted_list = sorted(media_list,
                         key=lambda media: media.score,
                         reverse=True)

    return sorted_list


def match_genre(user_genres, media, partial_match):
    media_genres = get_lowercase_genres(media.genres)

    for genre in user_genres:
        if partial_match:
            return genre[0] in media_genres
        else:
            if genre not in media_genres:
                return False
    return True


def filter_genre(user_genre_args, media_list, partial_match):
    return [media for media in media_list if match_genre(
        get_user_genres(user_genre_args),
        media,
        partial_match)]


query_url = 'https://graphql.anilist.co'
anilist_genres = get_anilist_genres()


def main():
    pass


if __name__ == '__main__':
    main()
