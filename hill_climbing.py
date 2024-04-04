from functions import successor,count_threats



start_state = [3,3,0,1]
neigohbor = successor(start_state)

for j in range(0,2):
    print(neigohbor[j])
    
