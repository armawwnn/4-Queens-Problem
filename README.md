
# 4-Queen Problem Solver with Metaheuristic Algorithms

## Introduction
This repository contains Python code to solve the 4-Queen problem using metaheuristic algorithms.

## Problem Statement
The 4-Queen problem involves placing 4 queens on a 4x4 chessboard such that no two queens threaten each other.

## Approach
This project implements the following metaheuristic algorithms to solve the 4-Queen problem:
- Hill Climbing Algorithm
- Genetic Algorithm
- Simulated Annealing

## How to Use
1. Clone the repository to your local machine.
2. Install the necessary dependencies (if any).
3. Run the Python scripts for each algorithm to solve the 4-Queen problem.

## Dependencies
- Python 3

## Algorithms
### Hill Climbing
![image](https://github.com/armawwnn/4-Queens-Problem/assets/55153680/4de848b2-e7ec-4eaa-8ff1-a33bc0abfcce)
The Hill Climbing algorithm attempts to maximize a heuristic function by making incremental changes to the current state. However, it has some limitations:
- **Local Maxima/Minima**: Hill Climbing can get stuck in local maxima or minima, preventing it from reaching the global optimum solution.
- **Plateaus**: In case of plateaus where multiple neighboring states have the same heuristic value, Hill Climbing may struggle to make progress.

#### Variants of Hill Climbing:
1. **Hill Climbing Random Restart:**
   - This variant of Hill Climbing involves randomly restarting the search from different initial points.
   - It aims to overcome local optima by allowing the algorithm to explore multiple regions of the search space.
   - It repeats the Hill Climbing process from different starting points until a satisfactory solution is found or a maximum number of iterations is reached.

2. **Hill Climbing Stochastic:**
   - Stochastic Hill Climbing introduces randomness in the selection of the next move.
   - Instead of always selecting the best neighbor, it randomly selects a neighbor and evaluates whether it improves the current solution.
   - This randomness can help escape local optima and explore a broader area of the search space.

3. **Hill Climbing First Choice:**
   - First Choice Hill Climbing improves efficiency by only considering the first neighbor that improves the current solution.
   - It avoids exhaustive evaluation of all neighbors, making it computationally faster.
   - However, it might not always lead to the best solution since it settles for the first improving move it encounters.

4. **Hill Climbing Steepest Ascent:**
   - Steepest Ascent Hill Climbing always selects the neighbor that provides the highest improvement in the objective function.
   - It exhaustively evaluates all neighbors to find the steepest ascent direction.
   - While this approach can lead to better solutions compared to other variants, it can be computationally expensive, especially in high-dimensional search spaces.

Steepest Ascent Hill Climbing has a probability of around 40% to find the global optimum in the 4-Queen problem. However, with the First Choice Hill Climbing algorithm, this probability decreases to approximately 30% for finding the global optimum.
