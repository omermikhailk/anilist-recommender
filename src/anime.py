class Anime():
    """A class representing an anime on AL.

    Attributes:
        title (dict[str: str]): The title of the anime (in both Romaji and
            English).
        episodes (int): The number of episodes the anime has.
        adult (bool): Whether the anime is rated adult or not.
        genres (list[str]): A list of genres which fit the anime.
        description (str): A description of the anime.
        score (int): An average score of the anime on AL.
    """
    def __init__(self,
                 title: dict[str: str],
                 episodes: int,
                 adult: bool,
                 genres: list[str],
                 description: str,
                 score: int):
        """Initialises the `Anime` class.

        Args:
            title (dict[str: str]): The title of the anime (in both Romaji and
                English).
            episodes (int): The number of episodes the anime has.
            adult (bool): Whether the anime is rated adult or not.
            genres (list[str]): A list of genres which fit the anime.
            description (str): A description of the anime.
            score (int): An average score of the anime on AL.
        """
        self.title = title
        self.episodes = episodes
        self.adult = adult
        self.genres = genres
        self.description = description
        self.score = score

    def __repr__(self):
        return (f'Anime({self.title}, {self.episodes}, {self.adult}, )'
                f'{self.genres}, {self.description}, {self.score}')
