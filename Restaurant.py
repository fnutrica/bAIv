import random
import math

class Restaurant(object):

    def __init__(self, price, behavioral):
        self.behavioral = behavioral
        self.price = price

    def getMinTip(self):
        return self.minTip