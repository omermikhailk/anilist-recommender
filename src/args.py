"""Handles command line arguments from the user."""


import prep
import argparse


program_description = '''
Generates anime/manga recommendations based on preferences which the user
can provide, if they would like to.

The only required values are the user's AniList username and the type of
media (anime or manga).

Optional arguments include:

* The preferred number of recommendations you would like to receive.
* Preferred genres (written like --genre slice of life --genre comedy, etc.)
    * Whether the user wants a full match or a partial match of genres. The
      default is a full match. If partial match is selected then only one
      genre should be given as the input.
    * The full list of available genres on AniList are:
        - Action           - Adventure        - Comedy
        - Drama            - Ecchi            - Fantasy
        - Hentai           - Horror           - Mahou Shoujo
        - Mecha            - Music            - Mystery
        - Psychological    - Romance          - Sci-Fi
        - Slice of Life    - Sports           - Supernatural
        - Thriller
* A lower bound on the number of episodes/chapters/volumes
* An upper bound on the number of episodes/chapters/volumes
* Whether the user is okay with series marked as 'Adult' on AL

Using these options a list of anime/manga are returned, along with some
information about them.
'''

help_username = 'An AniList username.'
help_type = ('The type of media (anime or manga) that the user is interested '
             'in.')
help_count = ('The number of recommendations you would like to receive '
              '(default is 5).')
help_genre = 'One or more AniList genres.'
help_partial_match = ('Whether the user wants a partial match of genres '
                      '(default false).')
help_lower_bound = 'A lower bound on the number of episodes/chapters/volumes.'
help_upper_bound = 'An upper bound on the number of episodes/chapters/volumes.'
help_adult = ('Whether the user is okay with series marked as \'Adult\' '
              '(default false).')


def add_args() -> argparse.Namespace:
    """Adds command line arguments that the user can use and returns them.

    Returns:
        args (argparse.Namespace): The arguments that the user entered
            and their values.
    """
    parser = argparse.ArgumentParser(
        description=program_description,
        formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument('username',
                        help=help_username)
    parser.add_argument('type',
                        help=help_type,
                        choices=['anime', 'manga'])
    parser.add_argument('-c',
                        '--count',
                        help=help_count,
                        default=5,
                        type=int)
    parser.add_argument('-g',
                        '--genre',
                        help=help_genre,
                        action='append',
                        nargs='+')
    parser.add_argument('-pm',
                        '--partial-match',
                        help=help_partial_match,
                        action="store_true",
                        default=False)
    parser.add_argument('-lb',
                        '--lower-bound',
                        help=help_lower_bound,
                        type=int)
    parser.add_argument('-ub',
                        '--upper-bound',
                        help=help_upper_bound,
                        type=int)
    parser.add_argument('-a',
                        '--adult',
                        help=help_adult,
                        action="store_true",
                        default=False)

    args = parser.parse_args()

    return args


def check_args(args: argparse.Namespace) -> None:
    """Makes sure that there's no errors in the values entered for the command
    line arguments.

    Args:
        args (argparse.ArgumentParser): The arguments that the user entered
            and their values.

    Raises:
        ValueError: if `upper-bound` <= 0
        ValueError: if `lower-bound` <= 0
        ValueError: if `upper-bound` < `lower-bound`
        ValueError: if `genre` is not a valid AniList genre
        ValueError: if `partial-match` is true but there are no genres
    """
    # `count`
    if args.count <= 0:
        raise ValueError('count must be greater than 0')

    # `upper-bound` and `lower-bound`
    lower_bound = args.lower_bound
    upper_bound = args.upper_bound

    if upper_bound is not None:
        if upper_bound <= 0:
            raise ValueError('upper-bound should be positive')

    if lower_bound is not None:
        if lower_bound <= 0:
            raise ValueError('lower-bound should be positive')

    if lower_bound is not None and upper_bound is not None:
        if lower_bound > upper_bound:
            raise ValueError('upper-bound should be greater than lower-bound')

    # `genre`
    if args.genre is not None:
        user_genres = prep.get_user_genres(args.genre)
        anilist_genres = prep.get_lowercase_genres(prep.anilist_genres)

        for genre in user_genres:
            if genre not in anilist_genres:
                raise ValueError(f'\'{genre}\' is not a valid AniList genre')
        
        # `partial-match`
        if args.partial_match and len(user_genres) > 1:
            raise ValueError(('only one genre input is supported with the '
                              '--partial-match flag'))
    else:
        if args.partial_match:
            raise ValueError('partial-match requires you to add genres')


def main():
    pass


if __name__ == '__main__':
    main()
