import random
import math

class Customer(object):

    def __init__(self, foodPref, expectedTip):
        self.foodPref = foodPref
        self.expectedTip = self.expectedTip

        self.experience = experience(price, randomTip)
        self.value = None

        self.ltm = random.randint(0,100) # likelihood to mutate
        self.ltc = random.randint(0,100) # likelihood to crossover

    def getExpectedTip(self):
        return self.expected_tip

    def getFoodPref(self, pref):
        return self.foodPref

    def setExpectedTip(self, tip):
        self.expectedTip = tip
        return self.expectedTip

    def setFoodPref(self, pref):
        self.foodPref = pref
        return self.foodPref

    def experience(self, price, randomTip):
        pricePaid = price + randomTip
        gap = self.expectedTip - randomTip
        self.experience = gap / pricePaid
        return self.experience

    def printCustomer(self):
        print("Expected Tip = ", self.expectedTip)
        print("Food Preference = ", self.foodPref)
        print("Heuristic = ", self.value)