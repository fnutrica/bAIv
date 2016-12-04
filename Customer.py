import random
import math

class Customer(object):

    def __init__(self, food_preferences, expected_tip):
        self.food_preferences = food_preferences
        self.expected_tip = self.expected_tip
        self.value = None
        self.ltm = random.randint(0,100) # likelihood to mutate
        self.ltc = random.randint(0,100) # likelihood to crossover

    def expected_tip(self):
        return self.expected_tip

    def set_expected_tip(self, tip):
        self.expected_tip = tip
        return self.expected_tip

    def set_food_preferences(self, pref):
        self.food_preferences = pref
        return self.food_preferences

#   move this to tipping_sim
    def mutation(self):
        mut = random.uniform(0.9, 1.1)
        self.expected_tip = self.expected_tip * mut
        return self

    def heuristic(self, price_paid, tip_paid):
        self.value = 1 - tip_paid/
        return 1- tip_paid/price_paid


    def printCustomer(self):
        print("Minimum Tip = ", self.minTip)
        print("Tipping Restaurant = ", self.preference, "%")
        print("Heuristic = ", self.value)