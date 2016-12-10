import random
import math
import Customer
import Restaurant

<<<<<<< Updated upstream
PRICE = 100
MAX = 1
MIN = 0
N_RESTAURANTS = 20
=======
MARKET_PRICE = 100
N_RESTAURANT = 10
>>>>>>> Stashed changes
N_CUSTOMERS = 10
MAX_GENERATIONS = 10

def tipping_sim():

    customer_pop = []
    restaurant_pop = []

    # generates random population of customers
    for i in range(0, N_CUSTOMERS):
<<<<<<< Updated upstream
        customer_pop.append(Customer.Customer())

    for i in range(0, N_RESTAURANTS):
        restaurant_pop.append(Restaurant.Restaurant())

    print("================ Initial States ================")

    for customer in customer_pop:
       print("Customer ", id(customer))
=======
        foodPref = random.uniform(1, 5)
        # expected value of random tip (between 0 and 100)
        expTip = 25
        cust_pop.append(Customer.Customer(foodPref, expTip))

    # generates random population of restaurants
    for i in range(0, N_RESTAURANT):
        randTip = random.uniform(0, 50)
        price = random.uniform(0, 100)
        rest_pop.append(Restaurant.Restaurant(randTip, price))

    print("================ Initial States ================")

    #############WORK FROM HERE

    for i in range(0,len(cust_pop)-1):
        curr = cust_pop[i]
        print("Customer #", i)
        curr.printCustomer()
>>>>>>> Stashed changes

    # always false for now
    foundEquilibrium = False
    count = 0

    while (not foundEquilibrium) and count < MAX_GENERATIONS:
        count += 1
        print("================ Generation ", count, " ================")

        #array of heuristics
        fits = [cust.value for cust in pop]

        print("Average fitness:", sum(fits) / len(fits))
        print("Max fitness:", max(fits))
        print("Min fitness:", min(fits))

        parentPool = selectParents(pop, fits)
        currPop = mateParents(parentPool)

        print(" ")
        printCustomers(currPop)

        pop.clear()
        pop.extend(currPop)

    print("================ Done ================")
    print("Summary...")
    print("Tipping Restaurant Customers: ")
    print("Non-Tipping Restaurant Customers: ")

    return count

def random_behavior():
    return random.uniform(-1, 1)

def printCustomers(neighList):
    for neigh in neighList:
        neigh.printCustomer()

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
