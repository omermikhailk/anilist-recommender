"""A class representing an user on AniList."""


import requests
from typing import Dict
from media import Anime, Manga
from prep import query_url


class User:
    """A class representing an user on AniList.

    Attributes:
        username (str): The user's AniList username.
    """
    def __init__(self, username: str) -> None:
        """Initialises the `User` class.

        Args:
            username (str): The user's AniList username.
        """
        self.username = username

    def __repr__(self) -> str:
        """Returns a string representation of the `User` class.

        Returns:
            str: A string representation of the `User` class and it's intialisation arguments.
        """
        return f'User({self.username})'

    def get_query_variables(self) -> Dict[str, int | str | None]:
        """Returns the variables required for the AL API query.

        Returns:
            Dict[str, int | str, None]: The variables required for the AL API query.
        """
        return {'page': 1,
                'perPage': 50,
                'userName': self.username,
                'type': None}

    def paginate(self, query: str, query_variables: dict) -> list[dict]:
        """Paginates through a user's media list using a given query to the API (`query`) and the variables required
        to do so (`query_variables`).

        If elements in the media list can be found they are returned. If not an empty list is returned, indicating
        that paginatnion has come to an end.

        Args:
            query (str): The query string that will be sent to the AL API.
            query_variables (dict): The variables required for the query to the AL API.

        Returns:
            results (list[dict]): This list either contains elements of the user's media list, or it is empty, thereby
            indicating that pagination has come to an end.
        """
        results = requests.post(query_url,
                                json={'query': query,
                                      'variables': query_variables}).json()
        results = results['data']['Page']

        if not results['mediaList']:
            results = []
            return results
        else:
            return results['mediaList']

    def get_anime_list(self, query: str) -> list[Anime]:
        """Paginates through the user's media list, only considering anime entries which are either 'Paused' or
        'Planning', and returns them as a list in the form of many `Anime` objects.

        The returned list of objects contains entry-specific information such as the information such as the title of
        the show, the number of episodes, etc.

        Args:
            query (str): The query string that will be sent to the AL API.

        Returns:
            anime_list (list[Anime]): A list containing the anime from the user's AL media list.
        """
        anime_list = []
        query_variables = self.get_query_variables()
        query_variables['type'] = 'ANIME'

        # We will cycle through every page (since we have to use pagination with the AniList API) and continue until
        # the results are exhausted.
        while True:
            if results := self.paginate(query, query_variables):
                pass
            else:
                break

            for entry in results:
                anime = entry['media']
                user_status = entry['status']
                if user_status in ('PLANNING', 'PAUSED'):
                    anime_list.append(Anime(anime['title'], user_status, anime['status'], anime['episodes'],
                                            anime['isAdult'], anime['genres'], anime['description'],
                                            anime['averageScore']))

            query_variables['page'] += 1

        return anime_list

    def get_manga_list(self, query: str) -> list[Manga]:
        """Paginates through the user's media list, only considering manga entries which are either 'Paused' or
        'PLanning', and returns them as a list in the form of many `Manga` objects.

        The returned list of objects contains entry-specific information such as the information such as the title of
        the manga, the number of chapters, etc.

        Args:
            query (str): The query string that will be sent to the AL API.

        Returns:
            manga_list (list[Manga]): A list containing the manga from the user's AL media list.
        """
        manga_list = []
        query_variables = self.get_query_variables()
        query_variables['type'] = 'MANGA'

        # We will cycle through every page (since we have to use pagination
        # with the AniList API) and continue until the results are exhausted.
        while True:
            if results := self.paginate(query, query_variables):
                pass
            else:
                break

            for entry in results:
                manga = entry['media']
                user_status = entry['userStatus']
                if user_status in ('PLANNING', 'PAUSED'):
                    manga_list.append(Manga(manga['title'], user_status, manga['status'], manga['chapters'],
                                            manga['volumes'], manga['isAdult'], manga['genres'], manga['description'],
                                            manga['averageScore']))

            query_variables['page'] += 1

        return manga_list


def main():
    pass


if __name__ == "__main__":
    main()
