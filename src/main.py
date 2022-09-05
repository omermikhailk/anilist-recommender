query = '''
    query ($page: Int, $perPage: Int, $userName: String, $type: MediaType) {
        Page (page: $page, perPage: $perPage) {
            mediaList (userName: $userName, type: $type) {
                media {
                    title {
                        english
                        romaji
                    }
                    status

                    episodes

                    chapters
                    volumes

                    isAdult

                    genres
                    description

                    averageScore
                }

                status
            }
        }
    }
'''


def main():
    pass


if __name__ == '__main__':
    main()
