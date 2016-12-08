import random
import math

class Restaurant(object):

    def __init__(self, randomTip, price):
        self.randomTip = randomTip
        self.price = price

    def getTip(self):
        return self.randomTip

    def getPrice(self):
        return self.price

    def setTip(self, tip):
        self.randomTip = tip
        return self.randomTip

    def setPrice(self, tip):
        self.randomTip = tip
        return self.randomTip