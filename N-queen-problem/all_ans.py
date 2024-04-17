
import matplotlib.pyplot as plt

from nqueen import NQueensState

states = []
seen_ans = []
n = 0
while n<=91:
    state = NQueensState.random_state(N=8)

    if state.conflicts() == 0 :
        if state.queens not in seen_ans:
            seen_ans.append(state.queens)
            state.plot()
            states.append(state)
            print(state)
            n +=1


