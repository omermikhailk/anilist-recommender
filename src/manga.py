class Manga():
    def __init__(self,
                 title: dict[str: str],
                 chapters: int,
                 volumes: int,
                 adult: bool,
                 genres: list[str],
                 description: str,
                 score: int):
        self.title = title
        self.chapters = chapters
        self.volumes = volumes
        self.adult = adult
        self.genres = genres
        self.description = description
        self.score = score

    def __repr__(self):
        return (f'Anime({self.title}, {self.chapters}, {self.volumes}), '
                f'{self.adult}, {self.genres}, {self.description}, '
                f'{self.score}')
