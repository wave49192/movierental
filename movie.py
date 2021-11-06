from typing import List


class Movie:
    """
    A movie available for rent.
    """

    # The types of movies (price_code).
    def __init__(self, title: str, year: int, genre: List[str]):
        # Initialize a new movie.
        self._title = title
        self._year = year
        self._genre = genre

    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def get_genre(self):
        return self._genre

    def __str__(self):
        return self.title
