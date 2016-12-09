import random
import math

FOOD_TYPE = {"Pizza": 20, "Burger": 25, "Indian": 30, "Shish": 35}
LOCATION = {"Urban": 30, "Sub": 25, "Rural": 20}


class Restaurant(object):

    def __init__(self, score = 0, food_type = None, location = None, service_lv = None):

        # Resturant Score
        if score != 0:
            self.score = score
        else:
            self.score = 2.5

        # Service Level
        if service_lv != None:
            self.service_lv = service_lv
        else:
            self.service_lv = random.randint(0, 100)

        # Food Type
        if food_type != None:
            self.food_type = food_type
        else:
            self.food_type = random.choice(FOOD_TYPE.keys())

        # Food Type
        if location != None:
            self.location = location
        else:
            self.location = random.choice(LOCATION.keys())

        self.price = unit_price()
        self.cost = unit_cost()

    def unit_price(self):
        self.price = 100
        return self.price

    def unit_cost(self):
        #Cost of Food
        food = FOOD_TYPE.get(self.food_type)
        
        # Cost of Rent
        rent = LOCATION.get(self.location)

        # Cost of Labor
        labor = int(self.service_lv * 0.3)

        self.cost = food + rent + labor

        return self.cost

    def printRestaurant(self):
        print("Score = ", self.score)
        print("Food Type = ", self.food_type)
        print("Location = ", self.location)
        print("Service Level = ", self.service_lv)

