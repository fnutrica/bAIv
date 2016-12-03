import random
import math

class Customer(object):

    def __init__(self, preference, minTip, behavioral, price):
        self.behavioral = behavioral
        self.price = price
        self.minTip = minTip
        self.preference = preference

        self.adjustedTip = self.adjustTip()
        self.value = self.heuristic()


    def minTip(self):
        return self.minTip

    def preference(self):
        return self.preference

    def set_minTip(self, tip):
        self.minTip = tip
        return self.minTip

    def set_preference(self, pref):
        self.preference = pref
        return self.preference

    def mutation(self):
        mut = random.uniform(0.9, 1.1)
        self.minTip = self.minTip * mut
        return self

    def adjustTip(self):
        self.adjustedTip = self.minTip + self.behavioral
        return self.adjustedTip

    def adjustPref(self, utility):
        self.preference += utility
        return self.preference

    def heuristic(self):
        self.value = self.price / (self.price + self.price * self.adjustedTip)
        return self.value

    def printCustomer(self):
        print("Minimum Tip = ", self.minTip)
        print("Tipping Restaurant = ", self.preference, "%")
        print("Heuristic = ", self.value)