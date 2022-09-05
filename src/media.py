"""Classes representing a general `Media` object on AniList and it's subsequent
`Anime` and `Manga` subclasses."""


from typing import Dict


class Media:
    """A class representing a base `Media` object on AniList, from which the
    `Anime` and `Manga` classes are derived.
    """
    def __init__(self,
                 title: Dict[str, str],
                 user_status: str,
                 media_status: str,
                 score: int,
                 genres: list[str],
                 description: str,
                 adult: bool,
                 episodes: None | int,
                 chapters: None | int,
                 volumes: None | int) -> None:
        """Initialises the Media class.

        Args:
            title (Dict[str, str]): The title of the media (in English
                and Romaji).
            user_status (str): The status of the media on the user's list.
            media_status (str): The status of the media i.e finished, airing,
                etc.
            score (int): The score of the media from 0 to 100.
            genres (list[str]): A list of genres that fit the media.
            description (str): A string describing the media.
            adult (bool): A boolean showing whether the media is rated `Adult`
                on AniList or not.
            episodes (None | int): The number of episodes the media has (anime
                specific).
            chapters (None | int): The number of chapters the media has (manga
                specific).
            volumes (None | int): The number of  volumes the media has (manga
                specific).
        """
        # General
        self.title = title
        self.user_status = user_status
        self.media_status = media_status
        self.score = score
        self.genres = genres
        self.description = description
        self.adult = adult

        # Anime specific
        self.episodes = episodes

        # Manga specific

        self.chapters = chapters
        self.volumes = volumes

    def __repr__(self) -> str:
        """Returns a string representing the `Media` object (or any
        subclasses).

        Returns:
            str: A string representing the `Media` object (or any subclassses)
                and it's initialisation arguments.
        """
        return (f'{self.__class__.__name__}({self.title}, {self.user_status}, '
                f'{self.media_status}, {self.score}, {self.genres}, '
                f'{self.description}, {self.adult}, {self.episodes}, '
                f'{self.chapters}, {self.volumes})')


class Anime(Media):
    """A class representing an `Anime` object on AniList. It is a subclasss of
    the `Media` class.

    Args:
        Media (class): A class representing a `Media` object on AniList.
    """
    def __init__(self,
                 title: Dict[str, str],
                 user_status: str,
                 media_status: str,
                 score: int,
                 genres: list[str],
                 description: str,
                 adult: bool,
                 episodes: int,
                 chapters=None,
                 volumes=None) -> None:
        """Initialisation of the `Anime` class

        Args:
            title (Dict[str, str]): The title of the anime (in English and
                Romaji).
            user_status (str): The status of the anime on the user's list.
            media_status (str): The status of the anime i.e finished, airing,
                etc.
            score (int): The score of the anime from 0 to 100.
            genres (list[str]): A list of genres that fit the anime.
            description (str): A string describing the anime.
            adult (bool): A boolean showing whether the anime is rated `Adult`
                on AniList or not.
            episodes (None): The number of episodes the anime has.
            chapters (int): The number of chapters the media has (manga
                specific). Inherited attribute, so it's default value is set to
                `None`.
            volumes (int): The number of volumes the media has (manga
                specific). Inherited attribute, so it's default value is set to
                `None`.
        """
        super().__init__(title,
                         user_status,
                         media_status,
                         score,
                         genres,
                         description,
                         adult,
                         episodes,
                         chapters,
                         volumes)


class Manga(Media):
    """A class representing a `Manga` object on AniList. It is a subclass of
    the `Media` class.

    Args:
        Media (class): A class representing a `Media` object on AniList.
    """
    def __init__(self,
                 title: Dict[str, str],
                 user_status: str,
                 media_status: str,
                 score: int,
                 genres: list[str],
                 description: str,
                 adult: bool,
                 chapters: int,
                 volumes: int,
                 episodes=None,) -> None:
        """Initialisation of the `Manga` class

        Args:
            title (Dict[str, str]): The title of the manga (in English and
                Romaji).
            user_status (str): The status of the manga on the user's list.
            media_status (str): The status of the manga i.e finished, airing,
                etc.
            score (int): The score of the manga from 0 to 100.
            genres (list[str]): A list of genres that fit the manga.
            description (str): A string describing the manga.
            adult (bool): A boolean showing whether the manga is rated `Adult`
                on AniList or not.
            episodes (None): The number of episodes the media has (anime
                specific). Inherited attribute, so it's default value is set to
                `None`.
            chapters (int): The number of chapters the manga has.
            volumes (int): The number of volumes the manga has.
        """
        super().__init__(title,
                         user_status,
                         media_status,
                         score,
                         genres,
                         description,
                         adult,
                         episodes,
                         chapters,
                         volumes)
