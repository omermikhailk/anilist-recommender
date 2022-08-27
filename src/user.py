"""A AniList user class."""


from anime import Anime
from manga import Manga
import requests


query_url = 'https://graphql.anilist.co'


class User:
    def __init__(self, username: str):
        self.username = username
        self.query_variables = {'page': 1,
                                'perPage': 50,
                                'userName': self.username}

    def __repr__(self):
        return f'User({self.username})'

    def paginate(self, query: str) -> list[dict]:
        """Paginates through a user's media list, using a given `query` string.

        Returns the media list elements if they can be found, otherwise an
        empty list is given back, indicating that the end of pagination has
        been reached.

        Args:
            query (str): The query string that will be sent to the AL API.

        Returns:
            list[dict]: Either a list containing the media list
            elements are sent, or an empty list is returned.
        """
        results = requests.post(query_url,
                                json={'query': query,
                                      'variables': self.query_variables})\
            .json()['data']['Page']

        if not results['mediaList']:
            return []
        else:
            return results['mediaList']

    def get_anime_list(self, query: str) -> list[Anime]:
        """Paginates through the user's media list, only considering anime
        entries, and returns them as a list in the form of many `Anime`
        objects.

        The returned list of objects contains information such as: titles
        (english and romaji), episodes, whether the anime is adult or not,
        genres, a description and it's average score.

        Args:
            query (str): The query string that will be sent to the AL API.

        Returns:
            anime_list (list[Anime]): A list containing the anime from the
                user's AL media list.
        """
        anime_list = []
        self.query_variables['type'] = 'ANIME'

        # We will cycle through every page (since we have to use pagination
        # with the AniList API) and continue until the results are exhausted
        while True:
            if results := self.paginate(query):
                pass
            else:
                break

            for entry in results:
                anime = entry['media']
                anime_list.append(Anime(anime['title'],
                                        anime['episodes'],
                                        anime['isAdult'],
                                        anime['genres'],
                                        anime['description'],
                                        anime['averageScore']))

            self.query_variables['page'] += 1

        return anime_list

    def get_manga_list(self, query: str) -> list[Manga]:
        """Paginates through the user's media list, only considering manga
        entries, and returns them as a list in the form of many `Manga`
        objects.

        The returned list of objects contains information such as: titles
        (english and romaji), number of chapters, number of volumes, whether
        the manga is adult or not, genres, a description and it's average
        score.

        Args:
            query (str): The query string that will be sent to the AL API.

        Returns:
            manga_list (list[Manga]): A list containing the manga from the
                user's AL media list.
        """
        manga_list = []
        self.query_variables['type'] = 'MANGA'

        # We will cycle through every page (since we have to use pagination
        # with the AniList API) and continue until the results are exhausted
        while True:
            if results := self.paginate(query):
                pass
            else:
                break

            for entry in results:
                manga = entry['media']
                manga_list.append(Manga(manga['title'],
                                        manga['chapters'],
                                        manga['volumes'],
                                        manga['isAdult'],
                                        manga['genres'],
                                        manga['description'],
                                        manga['averageScore']))

            self.query_variables['page'] += 1

        return manga_list
