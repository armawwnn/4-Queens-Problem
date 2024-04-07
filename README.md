
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

Steepest Ascent Hill Climbing has a probability of around 40% to find the global optimum in the 4-Queen problem. However, with the First Choice Hill Climbing algorithm, this probability decreases to approximately 30% for finding the global optimum.
