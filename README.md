# anilist-recommender

## What does this do?

This program takes a user's AniList username and aims to return titles on their
'Plan to watch' section as recommendations, based on their score. Additionally
it can futher filter any such entries by various factors such as:
- Preferred genres
- Whether the user wants a complete match or a partial match of genres
- How many recommendations the user wants
- Whether the user is okay with anime/manga marked as 18+
- A lower and/or upper bound on episodes/chapters/volumes

The program will then return:
- A list of anime/manga recommendations, alongside with some details about
them, such as their rating, their descriptions, etc.

## How do I use it?

`python main.py --help` will show a full list of the available arguments
and what they all do.

## How does this program work?

The program makes use of the AniList API for some tasks and is comprised of a
few files, each with a specific purpose.

- `media.py` contains a base class representing a media entry on AniList. From
this objects representing anime and manga entries on AniList can be derived.
- `user.py` is subsequently a user object, representing one on AniList.
- `args.py` deals with getting the command line arguments available for use
with the program.
- `prep.py` is a module for general utility functions, as well as some
miscellaenous ones.
- `filter.py` filters the entries from the 'Planned' section of a user's
AniList and returns only those entries that satisy their requirements

## Dependencies

These can be found in `pyproject.toml` and installed via `pip install .`.

## Meta

Since this project is mainly for learning purposes, I won't be aceepting pull
requests, however feel free to create issues for anything that you'd either
like to see added or are having issues with.
