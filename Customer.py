import random


class Customer(object):

    def __init__(self, food_pref=None, service_val=None, location_pref=None, pe_happiness=None):

        if food_pref is None:
            self.food_pref = {"Pizza": random.uniform(0, 1), "Indian": random.uniform(0, 1),
                              "Burger": random.uniform(0, 1), "Shish": random.uniform(0, 1)}
        else:
            self.food_pref = food_pref

        if self.service_val is None:
            self.service_val = random.uniform(0, 1)
        else:
            self.service_val = service_val

        if food_pref is None:
            self.location_pref = {"Urban": random.uniform(0, 1), "Sub": random.uniform(0, 1),
                                  "Rural": random.uniform(0, 1)}
        else:
            self.location_pref = location_pref

        if pe_happiness is None:
            self.pe_happiness = random.uniform(0, 1)
        else:
            self.pe_happiness = pe_happiness

        self.expected_scores = []

    # service level currently carries a lot less weight than the other 2 params
    def set_expectations(self, restaurant):
        self.expected_scores.push({"restaurant": restaurant, "expectation":
                                                self.food_pref[restaurant.food_type] + \
                                               self.service_val * restaurant.service_lv + \
                                               self.location_pref[restaurant.location]})
        return

    def score_restaurant(self, restaurant):

        if restaurant.tip:
            additional_price = random.randint(-10, 10)
            actual_score = self.expected_scores[restaurant] + additional_price*self.pe_happiness
            restaurant.score = (restaurant.score*restaurant.n_scores + actual_score)/(restaurant.n_scores+1)
            restaurant.n_scores += 1
        return




