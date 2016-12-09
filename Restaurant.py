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
            self.food_type = {"Pizza": random.randint(0, 1),
                              "Indian": random.randint(0, 1),
                              "Burger":random.randint(0,1),
                              "Shish":random.randint(0,1)}

        # Food Type
        if location != None:
            self.location = location
        else:
            self.food_type = {"Urban": random.randint(0, 1),
                              "Sub": random.randint(0, 1),
                              "Rural": random.randint(0, 1)}

    def printRestaurant(self):
        print("Score = ", self.score)
        print("Food Type = ", self.food_type)
        print("Location = ", self.location)
        print("Service Level = ", self.service_lv)

