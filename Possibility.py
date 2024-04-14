from hill_climbing import *



number_loop = 10000
fail = 0
succ = 0
steps = 0

i=0
while i < number_loop:
    i +=1
    resault,step = hill_climbing_first_choice(generate_board())
    steps = steps+step
    if calculate_attacks(resault) == 0:
        succ +=1
    else:
        fail +=1
print(f'Run for {number_loop} times')
print("first_choice")
print("fail: ",fail/number_loop*100)
print("sucss: " ,succ/number_loop*100)
print('Avg steps that take : ',steps/number_loop)
print('_____________')


fail = 0
succ = 0
steps = 0

i=0
while i < number_loop:
    i +=1
    resault,step = hill_climbing_steepest_acent(generate_board())
    steps = steps+step
    if calculate_attacks(resault) == 0:
        succ +=1
    else:
        fail +=1

print(f'Run for {number_loop} times')
print("steepest_acent")
print("fail: ",fail/number_loop*100)
print("sucss: " ,succ/number_loop*100)
print('Avg steps that take : ',steps/number_loop)
print('_____________')


fail = 0
succ = 0
steps = 0
i=0
while i < number_loop:
    i +=1
    resault,step = hill_climbing_stochastic(generate_board())
    steps = steps+step
    if calculate_attacks(resault) == 0:
        succ +=1
    else:
        fail +=1
print(f'Run for {number_loop} times')
print("stochastic")
print("fail: ",fail/number_loop*100)
print("sucss: " ,succ/number_loop*100)
print('Avg steps that take : ',steps/number_loop)
print('_____________')
