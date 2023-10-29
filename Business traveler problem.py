import matplotlib.pyplot as plt
import random

# Generation of the initial population.
def generate_population(population_size, cities): #1 population size, number of chromosomes in the population 2 list of cities (indexes) to visit
  population = []  # generated chromosomes are stored here, route to visit
  for i in range(population_size):
      chromosome = cities.copy() 
      random.shuffle(chromosome) #a copy of the list of cities (indexes) is created which is then mixed, one chromosome
      population.append(chromosome)
  return population

# Fitness calculation (route length). 
def fitness(chromosome, distances): #chromosome=route, distances distance matrix
  total_distance = 0
  for i in range(len(chromosome)-1): #find the distance between cities (pair) except the first and last
    city1 = chromosome[i]
    city2 = chromosome[i+1]
    total_distance += distances[city1][city2]
  total_distance += distances[chromosome[-1]][chromosome[0]] #distance from last to first, closing the loop
  return total_distance

# Performing a crossover operation.
def crossover(parent1, parent2):
  child = parent1.copy() # a child is created
  start_index = random.randint(0, len(parent1)-1)
  end_index = random.randint(start_index, len(parent1)) #take the area over which genes will be exchanged
  for i in range(start_index, end_index):
    if parent2[i] not in child[start_index:end_index]: #check whether the par2 gene is present on the route section (st-end), if it is missing, it will be added to the appropriate place
      index = child.index(parent2[i]) #find the parent2 gene index in the child’s route
      child[i], child[index] = child[index], child[i] # genes in this region change like in parent2, with movement inside to save the route
  return child

# Performing a mutation operation. 
def mutation(chromosome):    #2 random genes are selected and swapped so as not to get stuck in the local optimum
  index1 = random.randint(0, len(chromosome)-1)  #len()-1, since genome length = cities, and indices start from 0
  index2 = random.randint(0, len(chromosome)-1)
  chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
  return chromosome

# Execution of a genetic algorithm with a record of the history of evolution.
def genetic_algorithm(distances, population_size, generations):
  # Generation of the initial population. 
  cities = list(range(len(distances))) 
  population = generate_population(population_size, cities)

  # Recording the history of evolution. 
  history = []  #The best result for a generation is recorded here, everyone
  best_fitness = float('inf') #best track, infinity to ensure that the first generation is recorded as the best

  # Performing crossover, mutation and selection operations. 
  for i in range(generations):
    population = sorted(population, key=lambda x: fitness(x, distances)) #sorting routes in ascending order from best to worst by fitness function
    fitness_value = fitness(population[0], distances) #calculated for the best of his fitness

    # Recording best fitness and route.
    if fitness_value < best_fitness: # if the current value is better than the previous one, then it is recorded as the best
        best_fitness = fitness_value
        best_route = population[0]
        
        # Recording history. 
    history.append([i, fitness_value]) #new tuple, generation number and its value to track the result

    parents = population[:int(population_size/2)] #takes the best half (rounded down) and saves them
    offspring = [] #потомки
    for j in range(int(population_size/2)): #the second half is created from children, 2 random parents are taken
      parent1 = random.choice(parents)
      parent2 = random.choice(parents)
      child = crossover(parent1, parent2)
      if random.random() < 0.1: 
        child = mutation(child)
      offspring.append(child) 
    population = parents + offspring #a new list will be created from parents and descendants, preserving the best individuals from the past and introducing diversity in order to avoid premature convergence

    # Plotting the history of evolution. 
  plt.plot([h[0] for h in history], [h[1] for h in history])
  plt.xlabel('Generation') 
  plt.ylabel('Route cost') 
  plt.title('History of evolution') 
  plt.show()

  
  return best_route

distances = [
  [0, 93, 1, 55, 16, 69, 55, 90, 40, 58, 59, 27, 61, 68, 83, 100, 59, 96, 59, 38, 31, 35, 72, 98, 95, 34, 13, 77, 70, 45],
  [93, 0, 47, 62, 31, 75, 63, 20, 50, 25, 94, 94, 63, 57, 57, 8, 67, 19, 100, 61, 42, 94, 70, 31, 66, 94, 6, 48, 36, 63],
  [1, 47, 0, 13, 6, 66, 20, 53, 22, 33, 57, 29, 1, 7, 5, 37, 50, 81, 13, 19, 68, 75, 37, 91, 60, 5, 59, 67, 5, 1],
  [55, 62, 13, 0, 85, 29, 83, 62, 60, 94, 88, 46, 79, 62, 17, 49, 87, 30, 84, 72, 10, 24, 55, 15, 81, 68, 42, 13, 72, 17],
  [16, 31, 6, 85, 0, 68, 26, 99, 82, 41, 55, 57, 54, 45, 72, 19, 80, 7, 62, 51, 93, 21, 55, 64, 89, 71, 15, 74, 98, 17],
  [69, 75, 66, 29, 68, 0, 24, 31, 60, 2, 34, 34, 85, 38, 92, 45, 37, 44, 35, 10, 70, 74, 27, 3, 74, 11, 34, 32, 98, 39],
  [55, 63, 20, 83, 26, 24, 0, 65, 85, 49, 39, 92, 27, 34, 95, 67, 14, 77, 73, 96, 40, 82, 15, 16, 66, 6, 24, 31, 73, 67],
  [90, 20, 53, 62, 99, 31, 65, 0, 87, 58, 98, 37, 73, 98, 58, 10, 22, 82, 96, 72, 26, 78, 79, 21, 10, 98, 26, 87, 39, 53],
  [40, 50, 22, 60, 82, 60, 85, 87, 0, 82, 15, 99, 41, 68, 63, 99, 31, 47, 86, 84, 73, 23, 77, 28, 26, 22, 11, 70, 17, 92],
  [58, 25, 33, 94, 41, 2, 49, 58, 82, 0, 75, 27, 40, 86, 67, 79, 27, 47, 12, 83, 1, 15, 40, 12, 9, 71, 58, 64, 84, 29],
  [59, 94, 57, 88, 55, 34, 39, 98, 15, 75, 0, 87, 83, 34, 27, 93, 65, 47, 86, 87, 63, 20, 94, 58, 33, 15, 99, 83, 51, 41],
  [27, 94, 29, 46, 57, 34, 92, 37, 99, 27, 87, 0, 95, 76, 80, 1, 2, 64, 68, 17, 33, 84, 72, 10, 20, 3, 13, 25, 94, 44],
  [61, 63, 1, 79, 54, 85, 27, 73, 41, 40, 83, 95, 0, 5, 50, 33, 2, 73, 87, 22, 93, 100, 58, 68, 41, 60, 22, 31, 12, 21],
  [68, 57, 7, 62, 45, 38, 34, 98, 68, 86, 34, 76, 5, 0, 10, 32, 33, 28, 76, 12, 75, 79, 22, 62, 85, 51, 90, 18, 87, 77],
  [83, 57, 5, 17, 72, 92, 95, 58, 63, 67, 27, 80, 50, 10, 0, 20, 37, 28, 94, 26, 73, 41, 65, 80, 100, 57, 48, 11, 57, 21],
  [100, 8, 37, 49, 19, 45, 67, 10, 99, 79, 93, 1, 33, 32, 20, 0, 54, 11, 21, 18, 28, 81, 55, 61, 17, 99, 62, 95, 98, 15],
  [59, 67, 50, 87, 80, 37, 14, 22, 31, 27, 65, 2, 2, 33, 37, 54, 0, 43, 54, 49, 41, 9, 1, 7, 84, 38, 65, 83, 74, 76],
  [96, 19, 81, 30, 7, 44, 77, 82, 47, 47, 47, 64, 73, 28, 28, 11, 43, 0, 45, 59, 29, 52, 74, 48, 5, 74, 66, 79, 65, 40],
  [59, 100, 13, 84, 62, 35, 73, 96, 86, 12, 86, 68, 87, 76, 94, 21, 54, 45, 0, 4, 53, 14, 60, 24, 71, 96, 33, 22, 36, 65],
  [38, 61, 19, 72, 51, 10, 96, 72, 84, 83, 87, 17, 22, 12, 26, 18, 49, 59, 4, 0, 61, 69, 60, 60, 2, 67, 71, 94, 43, 27],
  [31, 42, 68, 10, 93, 70, 40, 26, 73, 1, 63, 33, 93, 75, 73, 28, 41, 29, 53, 61, 0, 54, 39, 37, 80, 34, 80, 98, 40, 62],
  [35, 94, 75, 24, 21, 74, 82, 78, 23, 15, 20, 84, 100, 79, 41, 81, 9, 52, 14, 69, 54, 0, 12, 37, 31, 81, 52, 100, 74, 37],
  [72, 70, 37, 55, 55, 27, 15, 79, 77, 40, 94, 72, 58, 22, 65, 55, 1, 74, 60, 60, 39, 12, 0, 50, 38, 80, 19, 16, 21, 56],
  [98, 31, 91, 15, 64, 3, 16, 21, 28, 12, 58, 10, 68, 62, 80, 61, 7, 48, 24, 60, 37, 37, 50, 0, 43, 48, 53, 46, 59, 21],
  [95, 66, 60, 81, 89, 74, 66, 10, 26, 9, 33, 20, 41, 85, 100, 17, 84, 5, 71, 2, 80, 31, 38, 43, 0, 81, 63, 44, 46, 17],
  [34, 94, 5, 68, 71, 11, 6, 98, 22, 71, 15, 3, 60, 51, 57, 99, 38, 74, 96, 67, 34, 81, 80, 48, 81, 0, 77, 17, 70, 78],
  [13, 6, 59, 42, 15, 34, 24, 26, 11, 58, 99, 13, 22, 90, 48, 62, 65, 66, 33, 71, 80, 52, 19, 53, 63, 77, 0, 91, 84, 68],
  [77, 48, 67, 13, 74, 32, 31, 87, 70, 64, 83, 25, 31, 18, 11, 95, 83, 79, 22, 94, 98, 100, 16, 46, 44, 17, 91, 0, 75, 98],
  [70, 36, 5, 72, 98, 98, 73, 39, 17, 84, 51, 94, 12, 87, 57, 98, 74, 65, 36, 43, 40, 74, 21, 59, 46, 70, 84, 75, 0, 17],
  [45, 63, 1, 17, 17, 39, 67, 53, 92, 29, 41, 44, 21, 77, 21, 15, 76, 40, 65, 27, 62, 37, 56, 21, 17, 78, 68, 98, 17, 0],
]
population_size = 100
generations = 600

best_route = genetic_algorithm(distances, population_size, generations)
print(f"Best route for {len(best_route)} cities: {best_route}")
print("Route cost:", fitness(best_route, distances))
