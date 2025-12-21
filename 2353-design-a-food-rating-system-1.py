from heapq import heappush, heappop


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

    '''

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_dict = {}
        self.cuisine_dict = {}
        n = len(foods)
        for i in range(n):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_dict[food] = [cuisine, rating]
            self.update_cuisine_rating(food, cuisine, rating)

    def update_cuisine_rating(self, food: str, cuisine: str, rating: int) -> None:
        if cuisine not in self.cuisine_dict:
            self.cuisine_dict[cuisine] = []

        heappush(self.cuisine_dict[cuisine], [-rating, food])

    def changeRating(self, food: str, newRating: int) -> None:
        if food not in self.food_dict:
            raise Exception("food does not exist")

        cuisine, _ = self.food_dict[food]
        self.food_dict[food] = [cuisine, newRating]
        self.update_cuisine_rating(food, cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        if cuisine not in self.cuisine_dict:
            raise Exception("cuisine does not exist")

        if len(self.cuisine_dict[cuisine]) == 0:
            raise Exception("no food exist for this cuisine")

        while self.cuisine_dict[cuisine]:
            highest_rating, highest_rated_food = self.cuisine_dict[cuisine][0]
            if -highest_rating != self.food_dict[highest_rated_food][1]:
                heappop(self.cuisine_dict[cuisine])
            else:
                return highest_rated_food

        return ''


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
