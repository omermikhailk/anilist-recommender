# anilist-recommender

## What does this do?

This is a program which aims to generate anime and manga recommendations based
on a few parameters that the user provides. The only necessary parameter is
the user's AniList username, however additional available parameters are:
- One or more genres
- How many recommendations the user wants
- Whether the user is okay with anime/manga marked as 18+
- Whether the user wants a complete match or a partial match of genres
- A lower and/or upper bound on episodes/chapters/volumes

The program will then return:
- A list of anime/manga recommendations, alongside with some details about
them, such as their rating, their descriptions, etc.

## How do I use it?

`python main.py --help`

```
usage: main.py [-h] [-g GENRE [GENRE ...]] [-pm] [-lb LOWER_BOUND] [-ub UPPER_BOUND] [-a]
               username {anime,manga}

Generates anime/manga recommendations based on preferences which the user
can provide, if they would like to.

The only required values are the user's AniList username and the type of
media (anime or manga).

Optional arguments include:

* Preferred genres (written like --genre slice of life --genre comedy, etc.)
    * Whether the user wants a full match or a partial match of genres. The
        default is a full match.
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

positional arguments:
  username              An AniList username.
  {anime,manga}         The type of media (anime or manga) that the user is interested in.

options:
  -h, --help            show this help message and exit
  -g GENRE [GENRE ...], --genre GENRE [GENRE ...]
                        One or more AniList genres.
  -pm, --partial-match  Whether the user wants a partial match of genres (default false).
  -lb LOWER_BOUND, --lower-bound LOWER_BOUND
                        A lower bound on the number of episodes/chapters/volumes.
  -ub UPPER_BOUND, --upper-bound UPPER_BOUND
                        An upper bound on the number of episodes/chapters/volumes.
  -a, --adult           Whether the user is okay with series marked as 'Adult' (default false).
```

## Dependencies

These can be found in `pyproject.toml` and installed via `pip install .`.

## Meta

Since this project is mainly for learning purposes, I won't be aceepting pull requests,
however feel free to create issues for anything that you'd either like to see added or are
having issues with.
