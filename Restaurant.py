import random

FOOD_TYPE = {"Pizza": 20, "Burger": 25, "Indian": 30, "Shish": 35}
LOCATION = {"Urban": 30, "Sub": 25, "Rural": 20}


class Restaurant(object):

    def __init__(self, food_type=random.choice(FOOD_TYPE.keys()), location=random.choice(LOCATION.keys()), service_lv=random.uniform(0, 1), tip = random.randint(0, 100)):
        self.price = self.unit_price()
        self.cost = self.unit_cost()
        self.score = 2.5
        self.n_scores = 0
        self.e_attributes = ["food_type", "location", "service_lv", "tip"] # can i have just the names as string?????

        self.service_lv = service_lv
        self.food_type = food_type
        self.location = location

        # Tip (80% chance to be tipping restaurant)
        if self.tip > 80:
            self.tip = False
        else:
            self.tip = True

    def get_e_attribute(self, index):
        return self.e_attributes[index]

    def set_e_attribute(self, index, attribute):
        if index == 1:
            self.food_type = attribute
        elif index == 2:
            self.location = attribute
        elif index == 3:
            self.service_lv = attribute
        else:
            self.tip = attribute

    def unit_price(self):
        self.price = 100
        return self.price

    def tot_cost(self, q_sold):
        #Cost of Food
        food = FOOD_TYPE.get(self.food_type)

        # Cost of Rent
        rent = LOCATION.get(self.location)

        # Cost of Labor
        labor = int(self.service_lv * 0.3)

        self.cost = food * q_sold + rent + labor * q_sold

        return self.cost

    def printRestaurant(self):
        print("Score = ", self.score)
        print("Food Type = ", self.food_type)
        print("Location = ", self.location)
        print("Service Level = ", self.service_lv)

