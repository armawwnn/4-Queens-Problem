from functions import successor,count_threats



start_state = [1,3,1,1]
neigohbor = successor(start_state)

def climbing(start):
    start_node = start
    while True:
        nei = successor(start_node)
        if count_threats(nei[0]) <= count_threats(nei[1]) and count_threats(nei[0]) < count_threats(start_node):
            start_node = nei[0]
            print(start_node)
         
        if count_threats(nei[1]) <= count_threats(nei[0]) and count_threats(nei[1]) < count_threats(start_node):
            start_node =  nei[1]
            print(start_node)

        else:
            return start_node

resault = climbing(start_state)
num = count_threats(resault)
print("resault : ")
print(resault,num)
