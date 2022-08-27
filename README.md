# anilist-recommender

## What does this do?

This is a program which aims to generate anime and manga recommendations based on a few parameters
that the user provides. The only necessary parameter is the user's AniList username, however
additional parameters are:
- One or more genres
- How many recommendations the user wants
- Whether the user is okay with anime/manga marked as 18+
- Whether the user wants a complete match or a partial match of genres
- A lower and/or upper bound on episodes/chapters/volumes

The program will then return:
- A list of anime/manga recommendations, alongside with some details about them, such as their
rating, their descriptions, etc.

## Dependancies

These can be found in `pyproject.toml` and installed via `pip install .`.

## Meta

Since this project is mainly for learning purposes, I won't be aceepting pull requests,
however feel free to create issues for anything that you'd either like to see added or are
having issues with.
