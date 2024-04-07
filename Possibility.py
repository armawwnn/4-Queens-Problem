from hill_climbing import *



number_loop = 1000
fail = 0
succ = 0

i=0
while i < number_loop:
    i +=1
    resault = hill_climbing_first_choice(generate_board())
    if calculate_attacks(resault) == 0:
        succ +=1
    else:
        fail +=1
print("first_choice")
print("fail: ",fail/number_loop*100)
print("sucss: " ,succ/number_loop*100)
print('_____________')


fail = 0
succ = 0

i=0
while i < number_loop:
    i +=1
    resault = hill_climbing_steepest_acent(generate_board())
    if calculate_attacks(resault) == 0:
        succ +=1
    else:
        fail +=1
print("steepest_acent")
print("fail: ",fail/number_loop*100)
print("sucss: " ,succ/number_loop*100)
print('_____________')


fail = 0
succ = 0

i=0
while i < number_loop:
    i +=1
    resault = hill_climbing_stochastic(generate_board())
    if calculate_attacks(resault) == 0:
        succ +=1
    else:
        fail +=1
print("stochastic")
print("fail: ",fail/number_loop*100)
print("sucss: " ,succ/number_loop*100)
print('_____________')

