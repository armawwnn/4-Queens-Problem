from functions import *

def localORglobal(state):
    if calculate_attacks(state) == 0:
        print("global optimum")
    else:
        print("local optimum")



def hill_climbing_first_choice(start):
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
                break

        if next_board is None:
            return current_board
        else:
            current_board = next_board
            current_attacks = min_attacks











def hill_climbing_steepest_acent(start):
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



fail = 0
suc = 0
n= 100000
c=0
while c<n:
    c += 1
    re = hill_climbing_steepest_acent(generate_board())
    if calculate_attacks(re) == 0:
        suc = suc+1
    else:
        fail = fail+1
print("steepest acent")
print("fail: ",fail/n*100)
print("sucss: " ,suc/n*100)

print("first choise ")


fail = 0
suc = 0
n= 100000
c=0
while c<n:
    c += 1
    re = hill_climbing_first_choice(generate_board())
    if calculate_attacks(re) == 0:
        suc = suc+1
    else:
        fail = fail+1

print("fail: ",fail/n*100)
print("sucss: " ,suc/n*100)
