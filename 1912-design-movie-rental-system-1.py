from typing import List
from heapq import heapify, heappop


class MovieRentingSystem:
    '''
    Init:
        - loop through each entry, and process them
        - We will have an unrented and rented hash to store
        - unrented: {movie: {shop: (price, shop, movie)}}
        - rented: {movie: {shop: (price, shop, movie)}}

    Search:
        - cheapest 5 shops with unrented copy of movie, sorted by (price, shop)
        - dynamically create a heap based on unrented movies using heapify?
        - heappop 5 times to get the cheapest 5 shops

    Rent:
        - rents movie from shop
        - remove movie from unrented hash, add movie into rented hash

    Drop:
        - return movie to shop
        - remove movie from rented hash, add movie into unrented hash

    Report:
        - return 5 cheapest rented movies sorted by (price, shop, movie)
        - search from rented hash

    This solution encountered TLE error as it isn't very efficient
    '''

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented, self.rented = {}, {}
        for shop, movie, price in entries:
            if movie not in self.unrented:
                self.unrented[movie] = {}

            self.unrented[movie][shop] = (price, shop, movie)

    def search(self, movie: int) -> List[int]:
        if movie not in self.unrented:
            return []
        result = []
        shops = []
        for shop, (price, shop, movie) in self.unrented[movie].items():
            shops.append((price, shop))

        heapify(shops)
        i = 0
        while shops and i < 5:
            _, shop_id = heappop(shops)
            result.append(shop_id)
            i += 1
        return result

    def rent(self, shop: int, movie: int) -> None:
        detail = self.unrented[movie][shop]
        del self.unrented[movie][shop]
        if movie not in self.rented:
            self.rented[movie] = {}

        self.rented[movie][shop] = detail

    def drop(self, shop: int, movie: int) -> None:
        detail = self.rented[movie][shop]
        del self.rented[movie][shop]
        if movie not in self.unrented:
            self.unrented[movie] = {}

        self.unrented[movie][shop] = detail

    def report(self) -> List[List[int]]:
        result = []
        rented_movies = []

        for shop_detail in self.rented.values():
            for price, shop, movie in shop_detail.values():
                rented_movies.append((price, shop, movie))

        heapify(rented_movies)
        i = 0
        while rented_movies and i < 5:
            _, shop_id, movie = heappop(rented_movies)
            result.append([shop_id, movie])
            i += 1
        return result

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()


movieRentingSystem = MovieRentingSystem(
    3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])

# return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
print(f'output: {movieRentingSystem.search(1)}, expected: [1,0,2]')

# Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(0, 1)

# Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.rent(1, 2)

# return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
print(f'output: {movieRentingSystem.report()}, expected: [[0, 1], [1, 2]]')

# Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.drop(1, 2)

# return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.
print(f'output: {movieRentingSystem.search(2)}, expected: [0,1]')
