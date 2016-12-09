import random


class Customer(object):

    def __init__(self, food_pref, service_val, location_pref, pe_happiness):
        self.food_pref = {"Pizza": random.randint(0, 1), "Indian": random.randint(0, 1), "Burger": random.randint(0, 1),
                          "Shish": random.randint(0, 1)}
        self.food_pref = food_pref
        self.service_val = service_val
        self.location_pref = location_pref
        self.pe_happiness = pe_happiness
        self.expected_scores = None

    def set_expectations(self, restaurant):
        self.expected_scores[id(restaurant)] = self.food_pref[restaurant.food_type] + \
                                               self.service_val * restaurant.service_lv + \
                                               self.location_pref[restaurant.location]
        return

    def score_restaurant(self, restaurant):
        if restaurant.tip:
            additional_price = random.randint(-10, 10)
            actual_score = self.expected_scores[restaurant] + additional_price*self.pe_happiness
            restaurant.score = (restaurant.score*restaurant.n_scores + actual_score)/(restaurant.n_scores+1)
            restaurant.n_scores += 1
        return




