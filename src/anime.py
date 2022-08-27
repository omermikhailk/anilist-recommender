class Anime():
    def __init__(self,
                 title: dict[str: str],
                 episodes: int,
                 adult: bool,
                 genres: list[str],
                 description: str,
                 score: int):
        self.title = title
        self.episodes = episodes
        self.adult = adult
        self.genres = genres
        self.description = description
        self.score = score

    def __repr__(self):
        return (f'Anime({self.title}, {self.episodes}, {self.adult}, )'
                f'{self.genres}, {self.description}, {self.score}')
