import random

PRICE = 100

PIZZA_COST = 2
BURGER_COST = 2.2
INDIAN_COST = 2.5
SHISH_COST = 2.7
ASIAN_COST = 3

CITY_RENT = 45
URBAN_RENT = 40
SUB_RENT = 30
RURAL_RENT = 20


class Restaurant(object):
    def __init__(self, food_type=None,
                 location=None,
                 service_lv=None,
                 tip=None,
                 profit=0,
                 marginal_profit=0,
                 units_sold=None):

        FOOD_TYPE = {"Pizza ": PIZZA_COST, "Burger": BURGER_COST, "Indian": INDIAN_COST, "Shish ": SHISH_COST, "Asian ": ASIAN_COST}
        LOCATION = {"City ": CITY_RENT, "Urban": URBAN_RENT, "Sub  ": SUB_RENT, "Rural": RURAL_RENT}

        self.price = self.unit_price()
        self.score = 2.5
        self.n_scores = 0

        if units_sold is not None:
            self.units_sold = units_sold
        else:
            self.units_sold = 0

        if service_lv is not None:
            self.service_lv = service_lv
        else:
            self.service_lv = random.uniform(0, 1)

        if food_type is not None:
            self.food_type = food_type
        else:
            self.food_type = random.choice(list(FOOD_TYPE.keys()))

        if location is not None:
            self.location = location
        else:
            self.location = random.choice(list(LOCATION.keys()))

        if tip is not None:
            self.tip = tip
        else:
            self.tip = random.uniform(0, 1)
            if self.tip > 0.8:
                self.tip = 0

        self.profit = profit
        self.marginal_profit = marginal_profit

        # Tip (80% chance to be tipping restaurant)
        self.e_attributes = [self.food_type, self.service_lv, self.location, self.tip]

    def get_e_attribute(self, index):
        return self.e_attributes[index]

    def set_e_attribute(self, index, attribute):
        if index == 0:
            self.food_type = attribute
        elif index == 1:
            self.service_lv = attribute
        elif index == 2:
            self.location = attribute
        else:
            self.tip = attribute

    def unit_price(self):
        self.price = 100
        return self.price

    def total_cost(self, q_sold):
        # Cost of Food
        FOOD_TYPE = {"Pizza ": PIZZA_COST, "Burger": BURGER_COST, "Indian": INDIAN_COST, "Shish ": SHISH_COST, "Asian ": ASIAN_COST}
        LOCATION = {"City ": CITY_RENT, "Urban": URBAN_RENT, "Sub  ": SUB_RENT, "Rural": RURAL_RENT}
        food = FOOD_TYPE.get(self.food_type)

        # Cost of Rent
        rent = LOCATION.get(self.location)

        # Cost of Labor
        labor = int(self.service_lv * 0.3)

        self.cost = food * q_sold + rent + labor * q_sold

        return self.cost

    def printRestaurant(self):
        print("Score =", "%.2f"%self.score, "     Food Type =", self.food_type, "     Location =", self.location, 
              "     Service Level =", "%.2f"%self.service_lv, "     Profit =", round(self.profit))

    def mutate(self):
        # choose from four attributes & make random change of >+/-10%
        rand = random.randint(0, 1)
        if rand == 0:
            self.service_lv += random.uniform(-0.1, 0.1)
        else:
            self.tip += random.randint(-5, 5)
