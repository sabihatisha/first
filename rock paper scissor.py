import random

user_wins=0
computer_wins=0
same_pinch=0
options= ["rock", "paper","scissor"]

while True:
    user_input = input("type rock/paper/ scissor or Q to quit ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue

    random_number= random.randint(0,2)
#R=0, P=1, S=2
    computer_pick= options[random_number]
    print("computer picked", computer_pick+".")

    if user_input=="rock" and computer_pick=='scissor':
        print('you wins')
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("you won!")
        user_wins+=1
    elif user_input=="scissor" and computer_pick=="paper":
        print("you won!")
        user_wins+=1
    elif user_input== computer_pick:
        print("it's a draw")
        same_pinch+=1
    else:
        print("you lost")
        computer_wins+=1


print("you win",user_wins, "times")
print("Computer win",computer_wins, "times")
print("draw",same_pinch,"times")
print("Goodbye!")