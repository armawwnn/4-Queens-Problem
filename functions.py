import random

def count_threats(queens):
    threats = 0
    n = len(queens)
    
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                threats += 1
                
    return threats


def generate_board():
    return [random.randint(0, 3) for _ in range(4)]




def calculate_attacks(board):
    attacks = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def generate_neighbors(board):
    neighbors = []
    for col in range(4):
        for row in range(4):
            if board[col] != row:
                neighbor = list(board)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors





