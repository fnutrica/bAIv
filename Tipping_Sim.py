import random
import math
import Customer
import Restaurant

PRICE = 100
MAX = 1
MIN = 0
N_RESTAURANT = 20
N_CUSTOMERS = 10
MAX_GENERATIONS = 10

def tipping_sim():

    cust_pop = []
    rest_pop = []

    for i in range(0, N_CUSTOMERS):
        minTip = random.uniform(MIN, MAX)
        behavioral = random_behavior()
        pop.append(Customer.Customer(init_pref, minTip, behavioral, PRICE))

    print("================ Initial States ================")

    for i in range(0,len(pop)):
        curr = pop[i]
        print("Customer #", i)
        curr.printCustomer()

    #always false
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
