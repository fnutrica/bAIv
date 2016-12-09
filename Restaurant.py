import random
import math

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
            type = ["Pizza", "Indian", "Burger", "Shish"]
            self.food_type = random.choice(type)

        # Food Type
        if location != None:
            self.location = location
        else:
            loc = ["Urban", "Sub", "Rural"]
            self.location = random.choice(loc)

        self.price = unit_price()
        self.cost = unit_cost()

    def unit_price(self):
        self.price = 100
        return self.price

    def unit_cost(self):
        #Cost of Food
        if self.food_type == "Pizza":
            food = 20
        elif self.location == "Indian":
            food = 30
        elif self.location == "Burger":
            food = 25
        else:
            food = 35
        
        # Cost of Rent
        if self.location == "Urban":
            rent = 30
        elif self.location == "Sub":
            rent = 25
        else:
            rent = 20

        # Cost of Labor
        labor = int(self.service_lv * 0.3)

        self.cost = food + rent + labor

        return self.cost

    def printRestaurant(self):
        print("Score = ", self.score)
        print("Food Type = ", self.food_type)
        print("Location = ", self.location)
        print("Service Level = ", self.service_lv)

