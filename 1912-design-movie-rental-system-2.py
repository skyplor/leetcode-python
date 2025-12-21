from typing import List
from collections import defaultdict
from heapq import heapify, heappop, heappush


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


    '''

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies, self.rented = defaultdict(list), set()
        self.prices = {}

        for shop, movie, price in entries:
            self.movies[movie].append((price, shop))
            self.prices[(shop, movie)] = price

        for movie in self.movies:
            self.movies[movie].sort()

    def search(self, movie: int) -> List[int]:
        result = []
        for _, shop in self.movies[movie]:
            if (shop, movie) not in self.rented:
                result.append(shop)
                if len(result) == 5:
                    break

        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        if (shop, movie) in self.rented:
            self.rented.remove((shop, movie))

    def report(self) -> List[List[int]]:
        rented_list = []
        for shop, movie in self.rented:
            price = self.prices[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()
        return [[shop, movie] for _, shop, movie in rented_list[:5]]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()


movieRentingSystem = MovieRentingSystem(
    3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])

# return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
print(f'output: {movieRentingSystem.search(1)}, expected: [1, 0, 2]')

# Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(0, 1)

# Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.rent(1, 2)

# return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
print(f'output: {movieRentingSystem.report()}, expected: [[0, 1], [1, 2]]')

# Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.drop(1, 2)

# return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.
print(f'output: {movieRentingSystem.search(2)}, expected: [0, 1]')
