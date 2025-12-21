from heapq import heappush, heappop, heapify
from collections import defaultdict


class FoodRatings:
    '''
    We can use 2 hashmaps
        - 1 hashmap `food_dict` to store the food and it's corresponding cuisine type + rating, i.e. key = food, value = [cuisine, rating]
        - 1 hashmap `cuisine_dict` to store the list of food for each cuisine and its rating, i.e. key = cuisine, value = [[-rating_1, food_1], [-rating_2, food_2]]

    Note that we need to multiply rating by `-1` because we want a max_heap

    In init, we first create the 2 hashmaps, then have a loop of length `n` that assigns the corresponding keys and values to the hashmaps accordingly
    In changeRating,
        - we will first retrieve the corresponding food to get its cuisine
        - Next, using the cuisine, we search for the food in `cuisine_dict` and we heappush the new food and rating in

    In highestRated, we will just retrieve from `cuisine_dict` and get the first element. We then need to double check with the rating in food_dict and if it matches, this is the most current rating. If it isn't, then we need to heappop it since it is stale data then we get the next element

    Optimizations to improve the execution time:
        - Use tuple instead of list to store the value of food_dict and cuisine_dict entries
        - Use heapify instead of individual heappush in __init__
        - Update while loop in highestRated to compare using the elements directly instead of first assigning to variables
    '''

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_dict = {}
        self.cuisine_dict = defaultdict(list)
        n = len(foods)
        for i in range(n):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_dict[food] = (cuisine, rating)
            self.cuisine_dict[cuisine].append((-rating, food))

        for cuisine in self.cuisine_dict:
            heapify(self.cuisine_dict[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        if food not in self.food_dict:
            raise Exception("food does not exist")

        cuisine, _ = self.food_dict[food]
        self.food_dict[food] = (cuisine, newRating)
        heappush(self.cuisine_dict[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while -self.cuisine_dict[cuisine][0][0] != self.food_dict[self.cuisine_dict[cuisine][0][1]][1]:
            heappop(self.cuisine_dict[cuisine])
        return self.cuisine_dict[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


# foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
# cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
# ratings = [9, 12, 8, 15, 14, 7]
# obj = FoodRatings(foods, cuisines, ratings)
# cuisine = "korean"
# param_2 = obj.highestRated(cuisine)
# print(f'output: {param_2}, expected: kimchi')
# cuisine = "japanese"
# param_2 = obj.highestRated(cuisine)
# print(f'output: {param_2}, expected: ramen')
# obj.changeRating("sushi", 16)
# cuisine = "japanese"
# param_2 = obj.highestRated(cuisine)
# print(f'output: {param_2}, expected: sushi')
# obj.changeRating("ramen", 16)
# cuisine = "japanese"
# param_2 = obj.highestRated(cuisine)
# print(f'output: {param_2}, expected: ramen')


foods = ["emgqdbo", "jmvfxjohq", "qnvseohnoe", "yhptazyko", "ocqmvmwjq"]
cuisines = ["snaxol", "snaxol", "snaxol", "fajbervsj", "fajbervsj"]
ratings = [2, 6, 18, 6, 5]
obj = FoodRatings(foods, cuisines, ratings)
obj.changeRating("qnvseohnoe", 11)
param_2 = obj.highestRated("fajbervsj")
print(f'output: {param_2}, expected: yhptazyko')
obj.changeRating("emgqdbo", 3)
obj.changeRating("jmvfxjohq", 9)
obj.changeRating("emgqdbo", 14)
param_2 = obj.highestRated("fajbervsj")
print(f'output: {param_2}, expected: yhptazyko')
param_2 = obj.highestRated("snaxol")
print(f'output: {param_2}, expected: emgqdbo')
