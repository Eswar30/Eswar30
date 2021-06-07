# Extercise 6
# Snake Water Gun

# s = "Snake"
# w = "Water"
# g = "Gun"

import random
a = ["Snake","Water","Gun"]
"""
snake vs water : snake
water vs Gun : water
snake vs Gun : Gun
"""
tie = 0
no = 0
n = 10
print("Game starts now:\n")
while(n>0):
    n = n-1
    # print(n)
    c = random.choice(a)
    i = input("Select:\ns for Snake,\nw for Water,\ng for Gun\n")
    # print(a)
    if i == c:  #
        print("Tie")
        tie = tie + 1
    elif i == "s" and c == "Water":
        print("You won")
        no = no +1
    elif i == "w" and c == "Gun":
        print("You won")
        no = no +1
    elif i == "g" and c == "Snake":
        print("You Won")
        no = no +1
    elif c =="Snake"and i == "w":
        print("Opponent wins")
    elif c =="Water"and i == "g": 
        print("Opponet wins")
    elif c =="Gun"and i == "s" :
        print("Opponet wins")
    else:
        print("Enter valied input")
o = 10 - no
print("Game Over")    
print(f"No of mathches you won : {no}\nNo of Tie brakes : {tie}\nNo of mathches opponent wins : {o}")
