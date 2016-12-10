import random
import math
import Customer
import Restaurant

PRICE = 100
MAX = 1
MIN = 0
N_RESTAURANTS = 10
N_CUSTOMERS = 20
MAX_GENERATIONS = 10

def tipping_sim():

    customer_pop = []
    restaurant_pop = []

    # generate random population
    customer_pop.extend(generate_random_pop(N_CUSTOMERS, Customer))
    restaurant_pop.extend(generate_random_pop(N_RESTAURANTS, Restaurant))

    print("================ Initial States ================")

    # for printing
    for i in range(0,len(restaurant_pop)-1):
        current = restaurant_pop[i]
        print("Restaurant #", i)
        current.printRestaurant()

    count = 0
    while count < MAX_GENERATIONS:
        count += 1

        # for customer choosing restaurant
        for customer in customer_pop:
            for restaurant in restaurant_pop:
                customer.set_expectations(restaurant)

                values = []

                for i in range(0, len(customer.expected_scores) - 1):
                    values.append(customer.expected_scores[i].expectation)

                index = rouletteSelect(values)
                choice = customer.expected_scores[index].restaurant

                # updates restaurant's score
                customer.score_restaurant(choice)

        print("================ Generation ", count, " ================")

        # evolve restaurant
        restaurantScores = [restaurant.score for restaurant in restaurant_pop]
        newRestaurants = evolve(restaurant_pop, restaurantScores)
        restaurant_pop.clear()
        restaurant_pop.extend(newRestaurants)

        # print restaurant attributes
        printRestaurants(restaurant_pop)

        print("Average score:", sum(restaurantScores) / len(restaurantScores))
        print("Max score:", max(restaurantScores))
        print("Min score:", min(restaurantScores))

        # randomly evolve customer (constant heuristics)
        customerHeuristics = [customer.heuristic for customer in customer_pop]
        newCustomers = evolve(customer_pop, customerHeuristics)
        customer_pop.clear()
        customer_pop.extend(newCustomers)

    print("================ Done ================")
    print("Summary...")
    print("Tipping Restaurant Customers: ")
    print("Non-Tipping Restaurant Customers: ")

    return count

def generate_random_pop(n, object):
    pop = []
    for i in range(0, n):
        pop.append(object.object())
    return pop

def evolve(pop, heuristic):
    newPop = []
    parentPool = selectParents(pop, heuristic)
    currPop = mateParents(parentPool)
    newPop.extend(currPop)
    return newPop

def random_behavior():
    return random.uniform(-1, 1)

def printRestaurants(neighList):
    for neigh in neighList:
        neigh.printRestaurant()

#============================================================================================

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

#############CHANGE THIS TO MATCH THE NEW CLASSES##############
def mateParents(parents):
    newPop = []
    for i in range(0, len(parents), 2):
        p1 = parents[i]
        p2 = parents[i+1]

        newOnes = crossover(p1, p2)
        newPop.extend(newOnes)

    for i in range(len(newPop)):
        nextOne = newPop[i]
        doMutate = random.random()

        if doMutate <= 0.5:
            newPop[i] = nextOne.mutation()

    return newPop

# cross point? not random right now bc there's only 2 variables
def crossover(customer1, customer2):
    pref1 = customer1.preference
    tip1 = customer1.minTip
    pref2 = customer2.preference
    tip2 = customer2.minTip

    #new random behavior assigned
    behav = random_behavior()
    newCust1 = Customer.Customer(pref1, tip2, behav, PRICE)
    newCust2 = Customer.Customer(pref2, tip1, behav, PRICE)

    return [newCust1, newCust2]
