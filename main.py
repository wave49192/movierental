# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer


def make_movies():
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("The Arrival"),
        catalog.get_movie("Particle Fever"),
        catalog.get_movie("The Legend of Sarila"),
        catalog.get_movie("Steve Jobs"),
        catalog.get_movie("Hacksaw Ridge")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
