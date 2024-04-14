from functions import *
import random

def hill_climbing_random_restart(start):
    resault , steps = hill_climbing_first_choice(start)
    while True: 
        if localORglobal(resault):
            return resault
        else :
            resault , steps = hill_climbing_first_choice(generate_board())





def hill_climbing_stochastic(start):
    current_board = start
    current_attacks = calculate_attacks(current_board)
    steps = 0

    while True:
        neighbors = generate_neighbors(current_board)
        next_board = None
        min_attacks = current_attacks
        better_neighbors = []
        for neighbor in neighbors:
            new_attacks = calculate_attacks(neighbor)
            if new_attacks < min_attacks:
                better_neighbors.append(neighbor)
                next_board = neighbor

        if next_board is None:
            return current_board,steps
        else:
            chosen_board = random.choice(better_neighbors)
            current_board = chosen_board
            current_attacks = calculate_attacks(chosen_board)
            steps +=1


def hill_climbing_first_choice(start):
    current_board = start
    current_attacks = calculate_attacks(current_board)
    steps = 0

    while True:
        neighbors = generate_neighbors(current_board)
        next_board = None
        min_attacks = current_attacks

        for neighbor in neighbors:
            new_attacks = calculate_attacks(neighbor)
            if new_attacks < min_attacks:
                min_attacks = new_attacks
                next_board = neighbor
                break

        if next_board is None:
            return current_board,steps
        else:
            current_board = next_board
            current_attacks = min_attacks
            steps +=1

def hill_climbing_steepest_acent(start):
    current_board = start
    current_attacks = calculate_attacks(current_board)
    steps = 0

    while True:
        neighbors = generate_neighbors(current_board)
        next_board = None
        min_attacks = current_attacks

        for neighbor in neighbors:
            new_attacks = calculate_attacks(neighbor)
            if new_attacks < min_attacks:
                min_attacks = new_attacks
                next_board = neighbor

        if next_board is None:
            return current_board,steps
        else:
            current_board = next_board
            current_attacks = min_attacks
            steps +=1



