import matplotlib.pyplot as plt
from functions import count_threats



y_val = [] 
x_val = []
count=0
for i in range(0, 4):
    for j in range(0, 4):  
        for k in range(0, 4):  
            for l in range(0, 4):  
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





