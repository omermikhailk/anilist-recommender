"""Handles command line arguments from the user."""


import prep
import argparse


program_description = '''
Generates anime/manga recommendations based on preferences which the user
can provide, if they would like to.

The only required values are the user's AniList username and the type of
media (anime or manga).

Optional arguments include:

* The preferred number of recommendations the user would like to receive.
* Preferred genres (written like `--genre slice of life --genre comedy` and so
  on.
    * Whether the user wants a strict match or not.

      By default the program does not use strict matching. If a user wants
      entries which have the `Shounen` and `Drama` genres, then the program
      looks for entries which satisfy those requirements. However any entries
      with additional genres do not have any adverse effect.

      When a strict match is preferred though, then the only matching entries
      are those, whose sole two genres are `Shounen` and `Drama`.
    * The full list of available genres on AniList are:
        - Action           - Adventure        - Comedy
        - Drama            - Ecchi            - Fantasy
        - Hentai           - Horror           - Mahou Shoujo
        - Mecha            - Music            - Mystery
        - Psychological    - Romance          - Sci-Fi
        - Slice of Life    - Sports           - Supernatural
        - Thriller
* A lower bound on the number of episodes/chapters/volumes.
* An upper bound on the number of episodes/chapters/volumes.
* Whether the user is okay with series marked as 'Adult' on AL.

Using these options a list of anime/manga are returned, along with some
information about them.
'''

help_username = 'An AniList username.'
help_type = ('The type of media (anime or manga) that the user is interested '
             'in.')
help_count = ('The number of recommendations the user would like to receive '
              '(default = 5).')
help_genre = 'One or more AniList genres.'
help_strict_match = ('Whether the user wants a strict match of genres or not '
                     '(default = False).')
help_lower_bound = 'A lower bound on the number of episodes/chapters/volumes.'
help_upper_bound = 'An upper bound on the number of episodes/chapters/volumes.'
help_adult = ('Whether the user is okay with series marked as \'Adult\' '
              '(default = False).')


def add_args() -> argparse.Namespace:
    """Adds command line arguments that the user can use and returns them. Also
    fixes any input problems, such as `args.genre` bieng a 2D list instead of a
    1D list.

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
    parser.add_argument('-sm',
                        '--strict-match',
                        help=help_strict_match,
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

    # Fixes the 2D list problem for `args.genre` and makes sure everything is
    # lowercase.
    # [['Slice', 'of', 'Life'], 'drama'] -> ['slice of life', 'drama']
    if args.genre is not None:
        args.genre = list(map(str.lower,
                              [' '.join(genre) for genre in args.genre]))

    return args


def check_args(args: argparse.Namespace) -> None:
    """Makes sure that there's no errors in the values entered for the command
    line arguments.

    Args:
        args (argparse.ArgumentParser): The arguments that the user entered
            and their values.

    Raises:
        ValueError: if `count` <= 0
        ValueError: if `upper-bound` <= 0
        ValueError: if `lower-bound` <= 0
        ValueError: if `upper-bound` < `lower-bound`
        ValueError: if `genre` is not a valid AniList genre
        ValueError: if `strict_match` is true but there are no genres
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
        anilist_genres_lowercase = list(map(str.lower, (prep.anilist_genres)))

        for genre in args.genre:
            if genre not in anilist_genres_lowercase:
                raise ValueError(f'\'{genre}\' is not a valid AniList genre')
    # `strict-match`
    else:
        if args.strict_match:
            raise ValueError('strict-match requires at least one genre')


def main():
    pass


if __name__ == '__main__':
    main()
