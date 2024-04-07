from functions import *

def hill_climbing(start):
    current_board = start
    current_attacks = calculate_attacks(current_board)

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
            return current_board
        else:
            current_board = next_board
            current_attacks = min_attacks


solution = hill_climbing([1,3,1,0])
print(solution)

