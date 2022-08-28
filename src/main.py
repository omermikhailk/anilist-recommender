from user import User


query = '''
    query ($page: Int, $perPage: Int, $userName: String, $type: MediaType) {
        Page (page: $page, perPage: $perPage) {
            mediaList (userName: $userName, type: $type) {
                media {
                    title {
                        english
                        romaji
                    }

                    episodes

                    chapters
                    volumes

                    isAdult

                    genres
                    description

                    averageScore
                }
            }
        }
    }
'''


def main():
    """
    user = User('omermikhailk')

    manga_list = user.get_manga_list(query)
    for manga in manga_list:
        print(manga)
    print('-\n-\n-\n-\n')
    anime_list = user.get_anime_list(query)
    for anime in anime_list:
        print(anime)
    """
    pass


if __name__ == '__main__':
    main()
