class Manga():
    """A class representing a manga on AL.

    Attributes:
        title (dict): The title of the manga (in both English and Romaji).
        chapters (int): The number of chapters the manga has.
        volumes (int): The number of volumes the manga has.
        adult (bool): Whether the manga is rated as adult or not.
        genres (list[str]): A list of genres that would fit the manga.
        description (str): A description for the manga.
        score (int): An average score of the manga on AL.
    """
    def __init__(self,
                 title: dict,
                 chapters: int,
                 volumes: int,
                 adult: bool,
                 genres: list[str],
                 description: str,
                 score: int) -> None:
        """Initialises the `Manga` class.

        Args:
            title (dict): The title of the manga (in both English and Romaji).
            chapters (int): The number of chapters the manga has.
            volumes (int): The number of volumes the manga has.
            adult (bool): Whether the manga is rated as adult or not.
            genres (list[str]): A list of genres that would fit the manga.
            description (str): A description for the manga.
            score (int): An average score of the manga on AL.
        """
        self.title = title
        self.chapters = chapters
        self.volumes = volumes
        self.adult = adult
        self.genres = genres
        self.description = description
        self.score = score

    def __repr__(self) -> str:
        """Returns a string representation of the `Manga` class.

        Returns:
            str: A representation of the `Manga` class.
        """
        return (f'Manga({self.title}, {self.chapters}, {self.volumes}), '
                f'{self.adult}, {self.genres}, {self.description}, '
                f'{self.score}')
