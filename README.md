# Evolutionary-Simulation

# Business Traveler Problem and Mountain Climbing Problem

This project demonstrates the solutions for two classic optimization problems - the Business Traveler Problem and the Mountain Climbing Problem. It provides Python code for solving these problems using genetic algorithms and hill climbing, respectively.

## Business Traveler Problem

The Business Traveler Problem involves finding the shortest route to visit a set of cities exactly once and return to the starting city. It uses a genetic algorithm to find an optimal route. The code for this problem can be found in the `business_traveler.py` file.

### Usage:

1. Define the distance matrix for cities in the `distances` variable.
2. Set the population size and number of generations in the `population_size` and `generations` variables.
3. Run the `genetic_algorithm` function with the distance matrix, population size, and number of generations to find the best route.

## Mountain Climbing Problem
The Mountain Climbing Problem is about finding the optimal combination of items to maximize a backpack's value without exceeding its capacity. The code for this problem can be found in the `mountain_climbing.py` file.

### Usage:
Define the backpack capacity (M) and the list of items with their weights and costs in the a variable.
Run the hill_climb function to find the best combination of items within the backpack's capacity.
