"""Takes entries from the user's AniList and filters them based on the criteria given in the command line arguments."""


from media import Anime, Manga
import prep


def sort_score(media_list: list[Anime | Manga]) -> list[Anime | Manga]:
    """Sorts a list of anime or manga, by their scores on AniList, in descending order.

    Args:
        media_list (list[Anime | Manga]): A list of anime or manga, containing instances of the `Anime`/`Manga` classes.

    Returns:
        list[Anime | Manga]: A sorted list of anime or manga entries, in descending order of their scores on AniList.
    """
    return sorted(media_list, key=lambda media: media.score, reverse=True)


def match_genre(user_genres: list[str], media: Anime | Manga, strict_match: bool) -> bool:
    """Given: a list of genres that the user is looking for, whether the user is okay with strict matches, and a piece
    of media, this function will pass/fail the media accordingly.

    The default matching behaviour is to use non-strict matching. All that needs to be ensured is that the genres
    which the user has picked need to be present in the media which is being evaluated. Any other genres do not have
    any effect on the matching process.

    However with `strict_match`, the aim is to have the media's genres precisely match with the user's genres, no
    extras at all.

    Args:
        user_genres (list[str]): A list of genres that the user is interested in.
        media (Anime | Manga): A piece of media on AniList.
        strict_match (bool): Whether the user is looking for strict matches or not.

    Returns:
        bool: Will return a boolean value, indicating whether the media entry satisfied the genre requirements or not.
    """
    media_genres = prep.get_list_lowercase(media.genres)

    if not strict_match:
        for genre in user_genres:
            if genre not in media_genres:
                return False
        return True
    else:
        for genre in media_genres:
            if genre not in user_genres:
                return False
        return True


def filter_genre(user_genres: list[str], media_list: list[Anime | Manga], strict_match: bool) -> list[Anime | Manga]:
    """Given: the user's list of preferred genres, a list of anime or manga, and whether the user is okay with strict
    matches or not, this function will filter the given media list and discard any entries that do not fit the genre
    requirements.

    Args:
        user_genres (list[str]): A list of the user's preferred genres
        media_list (list[Anime | Manga]): A list containing media entries.
        strict_match (bool): A boolean indicating whether the user is okay with strict matches or not.

    Returns:
        list[Anime | Manga]: The list of media entries filtered according to the genre requirements.
    """
    return [media for media in media_list if match_genre(user_genres, media, strict_match)]


def main():
    pass


if __name__ == "__main__":
    main()
