import random
import Customer
import Restaurant

PRICE = Restaurant.PRICE
N_RESTAURANTS = 50
N_CUSTOMERS = 100
N_ATTRIBUTES = 4  # exactly 4 attributes to be crossed for both Customer & Restaurant
MAX_GENERATIONS = 50

RESTAURANT_TYPES = ["Pizza  ", "Burger ", "African", "Shish  ", "Asian  "]
TYPE_COUNTS = {"Pizza  ": 0, "Burger ": 0, "African": 0, "Shish  ": 0,"Asian  ": 0}
TIPPING_COUNTS = {"Pizza  ": 0, "Burger ": 0, "African": 0, "Shish  ": 0,"Asian  ": 0}

def tipping_sim():
    sim_results = {}
    customer_pop = []
    restaurant_pop = []

    # generate random population
    for i in range(N_CUSTOMERS):
        customer_pop.append(Customer.Customer())
    for i in range(N_RESTAURANTS):
        restaurant_pop.append(Restaurant.Restaurant())

    countRestaurants(restaurant_pop)

    print("================ Initial States ================")

    # for printing
    for i in range(len(restaurant_pop)):
        current = restaurant_pop[i]
        current.printRestaurant()
    print("")

    count = 0
    while count < MAX_GENERATIONS:
        count += 1

        # customer chooses restaurant
        for customer in customer_pop:
            values = []
            for restaurant in range(len(restaurant_pop)):
                customer.set_expectations(restaurant_pop[restaurant])
                values.append(customer.expected_scores[restaurant]["expectation"])
            choice = rouletteSelect(values)
            # updates restaurant's score
            customer.score_restaurant(choice, PRICE)

        print("================ Generation ", count, " ================")

        # evolve restaurant
        restaurantProfits = [restaurant.profit for restaurant in restaurant_pop]
        parentRestaurants = selectParents(restaurant_pop, restaurantProfits)
        restaurant_pop = mateParents(parentRestaurants)

        # print restaurant attributes
        printRestaurants(restaurant_pop)

        # print generation summary
        print("")
        print("Average profit:", round((sum(restaurantProfits) / len(restaurantProfits))))
        print("Max profit    :", round(max(restaurantProfits)))
        print("Min profit    :", round(min(restaurantProfits)))
        print("")

        # randomly evolve customer (constant heuristics)
        customerHeuristics = []
        for customer in customer_pop:
            customerHeuristics.append(1)

        parentCustomers = selectParents(customer_pop, customerHeuristics)
        customer_pop = mateParents(parentCustomers)

    id = 1
    for restaurant in restaurant_pop:
        sim_results["restaurant " + str(id)] = {"profit": restaurant.profit}
        id += 1

    print("================ Summary ================")

    print("Generations :", count)
    print("Restaurants :", N_RESTAURANTS)
    print("Customers   :", N_CUSTOMERS)
    print("")
    print("Initial Restaurant Counts...")
    for i in range(5):
        print(RESTAURANT_TYPES[i], ":", TYPE_COUNTS[RESTAURANT_TYPES[i]], "    Tipping  :",
            TIPPING_COUNTS[RESTAURANT_TYPES[i]])

    resetCounts()
    countRestaurants(restaurant_pop)

    print("")
    print("Final Restaurant Counts...")
    for i in range(5):
        print(RESTAURANT_TYPES[i], ":", TYPE_COUNTS[RESTAURANT_TYPES[i]], "    Tipping  :",
            TIPPING_COUNTS[RESTAURANT_TYPES[i]])

    #return sim_results

def printRestaurants(neighList):
    for neigh in neighList:
        neigh.printRestaurant()

def countRestaurants(restaurant_pop):
    global RESTAURANT_TYPES, TYPE_COUNTS
    for r in restaurant_pop:
        r.update_tipping()
        for i in range(5):
            if r.food_type == RESTAURANT_TYPES[i]:
                TYPE_COUNTS[RESTAURANT_TYPES[i]] += 1
                countTipping(r)

def resetCounts():
    global TYPE_COUNTS, TIPPING_COUNTS
    newDict1 = TYPE_COUNTS.fromkeys(TYPE_COUNTS, 0)
    newDict2 = TIPPING_COUNTS.fromkeys(TIPPING_COUNTS, 0)
    TYPE_COUNTS = newDict1
    TIPPING_COUNTS = newDict2

def countTipping(restaurant):
    global TIPPING_COUNTS
    if restaurant.tipping is True:
        TIPPING_COUNTS[restaurant.food_type] += 1

# ============================================================================================

def rouletteSelect(valueList):
    totalValues = sum(valueList)
    pick = random.uniform(0, totalValues)
    s = 0
    for i in range(len(valueList)):
        s += valueList[i]
        if s >= pick:
            return i
    return len(valueList) - 1


def selectParents(states, fitnesses):
    """given a set of states, repeatedly select parents using roulette selection"""
    parents = []
    for i in range(len(states)):
        nextParentPos = rouletteSelect(fitnesses)
        parents.append(states[nextParentPos])
    return parents


def mateParents(parents):
    newPop = []

    # select parents for crossover
    for i in range(0, len(parents), 2):
        p1 = parents[i]
        p2 = parents[i + 1]

        # exactly 4 attributes to be swapped for both Customer and Restaurant
        n_cross = random.randint(0, N_ATTRIBUTES)

        if n_cross == 0:
            newPop.append(p1)
            newPop.append(p2)
        else:
            newOnes = crossover(p1, p2, n_cross)
            newPop.extend(newOnes)

    # mutate child
    for i in range(len(newPop)):
        nextOne = newPop[i]
        doMutate = random.random()

        # 50% chance of mutation

        if doMutate <= 0.1:
            nextOne.mutate()
            newPop[i] = nextOne

    return newPop

def crossover(agent1, agent2, n_cross):
    prob_cross = random.randint(0, 100)

    if prob_cross <= 101:  # for future use

        targets = random.sample(range(0, N_ATTRIBUTES), n_cross)

        for i in targets:
            attribute1 = agent1.get_e_attribute(i)
            attribute2 = agent2.get_e_attribute(i)
            agent1.set_e_attribute(i, attribute2)
            agent2.set_e_attribute(i, attribute1)

    return [agent1, agent2]


