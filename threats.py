import matplotlib.pyplot as plt


def count_threats(queens):
    threats = 0
    n = len(queens)
    
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                threats += 1
                
    return threats

y_val = [] 
x_val = []
count=0
for i in range(1, 5):
    for j in range(1, 5):  
        for k in range(1, 5):  
            for l in range(1, 5):  
                queens = [i,j,k,l]
                count = count+1
                x_val.append(count)

                threats = count_threats(queens)
                y_val.append(threats)
                print(queens)
                print("Number of threats:", threats)
                print("____________")
              



print(x_val)
x_values = x_val
y_values = y_val


plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-')

plt.xlabel('number of states')
plt.ylabel('Threat')
plt.title('4-q')

plt.grid(True)

plt.show()





