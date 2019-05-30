
#if the player don't switch
import random

p_win_not_switch=1/3
#it will alwas be a apro 33,333333% of win

n_trials=60000
win_always_switch=0
lose_always_switch=0

for x in range(0,n_trials):
    doors=["prize", 'empty', "empty"]
    random.shuffle(doors)
    chosen_door=random.randrange (3)

    if doors[chosen_door] == "prize":
        lose_always_switch=lose_always_switch  #because you are always changing here

    if doors [chosen_door] == "empty":
        win_always_switch = win_always_switch+1

p_win_switch = (win_always_switch*100)/n_trials
p_lose_switch = (lose_always_switch*100)/n_trials

print("Resultado: Em ", n_trials)
print('Quando não troca de porta a chance de ganhar é: ', p_win_not_switch*100, '%')
print('Quando sempre trocamos de porta: ', p_win_switch, '%')