from typing import List
import csv


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


class MovieCatalog:

    def __init__(self):
        self.movie_list = {}
        with open('movie.csv') as file:
            reader = csv.DictReader(file)
        for i in reader:
            self.movie_list[i["title"]] = {
                "#id": i["#id"],
                "year": i["year"],
                "genre": [j for j in i["genres"].split("|")]
            }

    def get_movie(self, title):
        movie = self.movie_list[title]
        return Movie(title, movie["year"], movie["genre"])
