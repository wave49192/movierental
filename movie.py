from typing import List


class Movie:
    """
    A movie available for rent.
    """

    # The types of movies (price_code).
    def __init__(self, title: str, year: int, genre: List[str]):
        # Initialize a new movie.
        self.title = title
        self.year = year
        self.genre = genre

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre

    def __str__(self):
        return self.title
