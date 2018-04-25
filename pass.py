import random
from math import floor

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello man"
population = []
population_size = 100




#This function will generate the intitial population
#The number and length of the intial individuals shall be provided
def generate_population(number): 
    for n in range(number):
        temp_var = []
        for l in range(len(target)):
            temp_var.append(geneSet[random.randrange(0, 55)])
            #print(''.join(temp_var))
        population.append(''.join(temp_var))


#The fitness value the genetic algorithm provides is the only feedback 
#the engine gets to guide it toward a solution.
#In this problem our fitness value is the total number 
#of letters in the guess that match the letter in the same 
#position of the password.
#this should be looped
def get_fitness(rand):  
    global target
    fitness_score = 0
    for d in range(len(target)):
        if rand[d] == target[d]:
            fitness_score += 1
    return fitness_score


#This is crossover function that generates a new offspring given a two parents
#if the crossover is sequetial, meaning it evaluates genes per gene.
#if both parents have a the fitness score the odds of having the 
#To give an edge the fittest organism i made a formula
def individual_crossover(indiv_1,indiv_1_fitness_score, indiv_2, indiv_2_fitness_score):
    child = ''
    ratio = []
    #Parent gene length check
    if len(indiv_1) == len(indiv_2):
        x = len(indiv_1) or len(indiv_2)
    else:
        print('One Parent Geneset is longer')
    

    if indiv_1_fitness_score == indiv_2_fitness_score:
        for i in range(x):
            pool = []
            pool.append(indiv_1[i])
            pool.append(indiv_2[i])
            child = child + pool[random.randrange(2)]
        #print("both")
        return child
    elif indiv_1_fitness_score > indiv_2_fitness_score:
        diff = indiv_1_fitness_score - indiv_2_fitness_score
        b = 50/len(target)
        ratio = [50+b, 50-b]
        for i in range(x):
            pool = []
            pool.append(indiv_1[i])
            pool.append(indiv_2[i])
            choose = random.randrange(0,100)
            if choose < ratio[0]:
                child = child + pool[0]
            else:
                child = child + pool[1]
        #print("Parent_1")
        return child
    elif indiv_1_fitness_score < indiv_2_fitness_score:
        diff = indiv_2_fitness_score - indiv_1_fitness_score
        b = 50/len(target)
        ratio = [50-b, 50+b]
        for i in range(x):
            pool = []
            pool.append(indiv_1[i])
            pool.append(indiv_2[i])
            choose = random.randrange(0,100)
            if choose < ratio[0]:
                child = child + pool[0]
            else:
                child = child + pool[1]
        #print('Parent_2')
        return child


def mass_crossover(population, fitness_board):
    fittest_score = max(fitness_board)                                              #the highest ranked individual points
    sum_fit = sum(fitness_board)                                                    #the total point in the fitness board     
    unfit = fitness_board.count(0)                                                  #individuals with 0 or no points
    while unfit == len(fitness_board):                                              #if all individual in the fitness board have zero a new population is generated
        print("Generating new parents")
        generate_population(population_size)
    cross_ratio = 100/sum_fit 
    cross_counter = 0
    new_pop = []
    for i in range(len(population)):
        for l in range(floor(fitness_board[i]*cross_ratio)):   
            new_pop.append(individual_crossover()) ### here the individual should search for a partner


def search_partner(male):
    sorted_fitboard = fitness_board.sort()
    
            






def mutation(population, rate):
    for i in range(rate):
        #print('Intitial population', population)
        indiv_num = random.randrange(len(population))
        indiv = population[indiv_num]
        #print('Individual is', indiv, ', With a number:', indiv_num)
        char_num = random.randrange(len(indiv))
        #print('\n')#indiv[char_num])
        re_indiv = indiv[0:indiv_num] + geneSet[random.randrange(55)] + indiv[indiv_num+1:len(indiv)]
        #print('Mutated',re_indiv)
        population[indiv_num] = re_indiv
    return population
      


generate_population(population_size)
solved = False

while solved == False:
    fitness_board = []
    for i in range(len(population)):
        rand = population[i]
        fitness_board.append(get_fitness(rand))
    print(fitness_board)
    solved = True


new = individual_crossover(population[0],fitness_board[0], population[1], fitness_board[1])
mutation(population, 1)