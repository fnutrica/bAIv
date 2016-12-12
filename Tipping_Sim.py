import random
import Customer
import Restaurant

PRICE = Restaurant.PRICE
MAX = 1
MIN = 0
N_RESTAURANTS = 30
N_CUSTOMERS = 1000
MAX_GENERATIONS = 10
N_ATTRIBUTES = 4  # exactly 4 attributes for both Customer & Restaurant


def tipping_sim():
    sim_results = {}
    customer_pop = []
    restaurant_pop = []

    # generate random population
    for i in range(N_CUSTOMERS):
        customer_pop.append(Customer.Customer())
    for i in range(N_RESTAURANTS):
        restaurant_pop.append(Restaurant.Restaurant())

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
        restaurantScores = [restaurant.profit for restaurant in restaurant_pop]
        parentRestaurants = selectParents(restaurant_pop, restaurantScores)
        restaurant_pop = mateParents(parentRestaurants)

        # print restaurant attributes
        printRestaurants(restaurant_pop)


        # print generation summary
        print("")
        print("Average score:", "%.2f"%(sum(restaurantScores) / len(restaurantScores)))
        print("Max score    :", "%.2f"%(max(restaurantScores)))
        print("Min score    :", "%.2f"%(min(restaurantScores)))
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

    print("================ Done ================")

    print("")

    return sim_results

def printRestaurants(neighList):
    for neigh in neighList:
        neigh.printRestaurant()


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


