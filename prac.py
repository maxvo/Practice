# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:57:15 2018
The Knapsack Problem:
In this problem, there is a set of box, each of this box has a value and a weight. On the other hand, you have a bag. It’s your bag. It has a limited weight capacity. Of course, you want to stuff it with as much value as possible. To sum it up, the problem is: what box should we chose to maximize the total value of the backpack.
https://blog.sicara.com/optimization-mutation-genetic-algorithm-40247f8ccb8
https://github.com/NicolleLouis/geneticAlgorithm/blob/master/KnapsackProblem_Mutation.py
@author: max
"""
import random
"""
Item Set:
It’s the name of the collection of boxes, it’s an array of boxes. A box has two parameters: a weight and a value.
"""
def generate_one_item(Max_Weight, Max_Value):
    item = []
    item.append(round(Max_Weight * random.random()))
    item.append(round(Max_Value * random.random()))
    return item

def generate_all_items(Number_of_item, Max_Weight, Max_Value):
    list_item = []
    for i in range(Number_of_item):
        list_item.append(generate_one_item(Max_Weight, Max_Value))
    return list_item
"""
Population:
Each individual is an array of boolean, the size of the item set. For each item, the corresponding value is true if the item is within the bag. On the opposite, it’s false if the item isn’t in the bag.
"""
def generate_one_individual(item_set):
    individual = []
    for i in range(len(item_set)):
        if (100 * random.random() < 50):
            individual.append(True)
        else:
            individual.append(False)
    return individual

def generate_first_population(item_set, size_of_population):
    population = []
    for i in range(size_of_population):
        population.append(generate_one_individual(item_set))
    return population
"""
Selection and Reproduction:
For a population, we select the best individuals and random individuals. After the selection, each couple of breeders creates 5 children. Children’s DNA is created randomly from parents’ DNA.
"""
def select_breeders (population_sorted, size_of_population):
    result = []
    best_individuals = size_of_population / 5
    lucky_few = size_of_population / 5
    for i in range(best_individuals):
        result.append(population_sorted[i])
    for i in range(lucky_few):
        result.append(random.choice(population_sorted))
    random.shuffle(result)
    return result

def create_child(individual1, individual2):
    result = []
    for i in range(len(individual1)):
        if (100 * random.random() < 50):
            result.append(individual1[i])
        else:
            result.append(individual2[i])
    return result

def create_children(breeders, number_of_child):
    result = []
    for i in range(len(breeders / 2)):
        for j in range(number_of_child):
            result.append(create_child(breeders[i], breeders[len(breeders) -1 -i]))
    return result
"""
Fitness:
For the fitness function, there are 2 cases. If the individual is bigger than the backpack capacity, the fitness is null. Else it’s equal to 2 times the value less the weight of the item.
"""
def fitness(individual, item_set):
    knapsack_capacity = round(total_weight_of_item_set(item_set) / 2)
    result = 0
    if (weight_of_individual(individual, item_set) <= knapsack_capacity):
        result = 2 * value_of_individual(individual, item_set) - weight_of_individual(individual, item_set)
    return result
print(generate_first_population(generate_all_items(10, 100, 123), 20))