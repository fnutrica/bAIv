import random


class Customer(object):

    def __init__(self, food_pref=None,
                 service_val=None,
                 location_pref=None,
                 pe_happiness=None):

        if food_pref is not None:
            self.food_pref = food_pref
        else:
            self.food_pref = {"Pizza": random.uniform(0, 1), "Indian": random.uniform(0, 1), "Burger": random.uniform(0, 1), "Shish": random.uniform(0, 1)}

        if service_val is not None:
            self.service_val = service_val
        else:
            self.service_val = random.uniform(0, 1)

        if location_pref is not None:
            self.location_pref = location_pref
        else:
            self.location_pref = {"Urban": random.uniform(0, 1), "Sub": random.uniform(0, 1), "Rural": random.uniform(0, 1)}

        if pe_happiness is not None:
            self.pe_happiness = pe_happiness
        else:
            self.pe_happiness = random.uniform(0, 1)

        self.expected_scores = []
        self.e_attributes = [self.food_pref, self.service_val, self.location_pref, self.pe_happiness]

    def get_e_attribute(self, index):
        return self.e_attributes[index]

    def set_e_attribute(self, index, attribute):
        if index == 0:
            self.food_pref = attribute
        elif index == 1:
            self.service_val = attribute
        elif index == 2:
            self.location_pref = attribute
        else:
            self.pe_happiness = attribute

    # service level currently carries a lot less weight than the other 2 params
    def set_expectations(self, restaurant):
        self.expected_scores.append({"restaurant": restaurant, "expectation":self.food_pref[restaurant.food_type] + self.service_val * restaurant.service_lv + self.location_pref[restaurant.location]})
        return

    def score_restaurant(self, choice):
        restaurant = self.expected_scores[choice]["restaurant"]
        additional_price = random.choice([-1, 1])*restaurant.tip
        actual_score = self.expected_scores[choice]["expectation"] + additional_price*self.pe_happiness
        restaurant.score = (restaurant.score*restaurant.n_scores + actual_score)/(restaurant.n_scores+1)
        restaurant.n_scores += 1
        return

    def mutate(self):
        # choose from four attributes & make random change of >+/-10%

        rand = random.randint(1,4)
        if rand == 1:
            self.food_pref["Pizza"] += random.uniform(-0.1,0.1)
            self.food_pref["Indian"] += random.uniform(-0.1, 0.1)
            self.food_pref["Burger"] += random.uniform(-0.1,0.1)
            self.food_pref["Shish"] += random.uniform(-0.1,0.1)
        elif rand == 2:
            self.service_val += random.uniform(-0.1,0.1)
        elif rand == 3:
            self.location_pref["Urban"] += random.uniform(-0.1,0.1)
            self.location_pref["Sub"] += random.uniform(-0.1,0.1)
            self.location_pref["Rural"] += random.uniform(-0.1,0.1)
        else:
            self.pe_happiness += random.uniform(-0.1,0.1)
