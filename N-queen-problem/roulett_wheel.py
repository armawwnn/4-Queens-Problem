import random

def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    #selected = []
    #for _ in range(1):
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind, fitness in zip(population, fitnesses):
        current += fitness
        if current > pick:
            selected = ind
            break
    return selected
