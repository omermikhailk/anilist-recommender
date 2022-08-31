"""Takes entries from the user's AniList and filters them based on the
criteria given in the command line arguments."""


from anime import Anime
from manga import Manga
import prep


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


def match_genre(user_genres: list[str],
                media: Anime | Manga,
                partial_match: bool) -> bool:
    """Given a list of genres that the user is looking for, whether the user
    is okay with partial matches, and a piece of media, this function will
    pass/fail the media accordingly.

    Args:
        user_genres (list[str]): A list of genres that the user is interested
            in.
        media (Anime | Manga): A piece of media on AniList.
        partial_match (bool): Whether the user is looking for partial matches
            or not.

    Returns:
        bool: Will return a boolean value, indicating whether the media entry
            satisfied the genre requirements or not.
    """
    media_genres = prep.get_lowercase_genres(media.genres)

    for genre in user_genres:
        if partial_match:
            return genre[0] in media_genres
        else:
            if genre not in media_genres:
                return False
    return True


def filter_genre(user_genre_args: list[list[str]],
                 media_list: list[Anime | Manga],
                 partial_match: bool) -> list[Anime | Manga]:
    """Given the user's command line input, for the genre flag, a list of anime
    or manga, and whether the user is okay with partial matches or not, this
    function will filter the given media list and discard any entries that do
    not fit the genre requirements.

    Args:
        user_genre_args (list[list[str]]): The command line input from the user
            for the `genre` flag. It is a 2D list, where every entry contains
            components/words comprising of a single genre.
        media_list (list[Anime  |  Manga]): A list containing media entries.
        partial_match (bool): A boolean indicating whether the user is okay
            with partial matches or not.

    Returns:
        list[Anime | Manga]: The list of media entries filtered according to
            the genre requirements.
    """
    return [media for media in media_list if match_genre(
        prep.get_user_genres(user_genre_args),
        media,
        partial_match)]
