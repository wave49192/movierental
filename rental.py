from movie import Movie
import logging


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def calculate_renter_point(self):
        frequent_renter_points = 0
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            frequent_renter_points += self.get_days_rented()
        else:
            frequent_renter_points += 1
        return frequent_renter_points

    def get_price(self):
        # award renter points
        return self.get_movie().get_price_code().price(self.days_rented)
