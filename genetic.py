import random

from phrase import Phrase, target
from helpers import summarize


population_size = 500
population = []
best_score = 0
generation_count = 1

# CREATE RANDOM POPULATION
for i in range(population_size):
    population.append(Phrase())

while best_score < len(target):
    # ACCESS FITNESS
    for i in range(population_size):
        population[i].get_fitness()

        if population[i].fitness > best_score:
            best_score = population[i].fitness
            summarize(generation_count,
                      population[i].get_contents(), best_score)

    # CREATE MATING POOL
    mating_pool = []
    parents = population[:]
    population = []

    # add phrases to the new mating pool according to their fitness, this weeds bad ones out
    for i in range(population_size):
        for j in range(parents[i].fitness):
            mating_pool.append(parents[i])

    for i in range(population_size):
        mother = random.choice(mating_pool)
        father = random.choice(mating_pool)

        child = mother.crossover(father)
        child.mutate()

        population.append(child)

    generation_count += 1
