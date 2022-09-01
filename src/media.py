from typing import Dict


class Media:
    def __init__(self,
                 title: Dict[str, str],
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
        """Returns a string representing the `Media` object (or any subclasses).

        Returns:
            str: A string representing the `Media` object (or any subclassses)
                and it's initialisation arguments.
        """
        return (f'{self.__class__.__name__}({self.title}, {self.score}, {self.genres}, '
                f'{self.description}, {self.adult}, {self.episodes}, '
                f'{self.chapters}, {self.volumes})')


class Anime(Media):
    def __init__(self,
                 title: Dict[str, str],
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
                        score,
                        genres,
                        description,
                        adult,
                        episodes,
                        chapters,
                        volumes)


class Manga(Media):
    def __init__(self,
                 title: Dict[str, str],
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
                        score,
                        genres,
                        description,
                        adult,
                        episodes,
                        chapters,
                        volumes)
