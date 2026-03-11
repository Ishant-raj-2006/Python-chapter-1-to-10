# We all have played a water gun game in our childhood if you Have not google the rules of this game and right by the program capital of playing this game with the US
'''
1 for snake 
-1 for water
0 for gun 
'''

import random

# mapping
choices = {
    1: "Snake 🐍",
    -1: "Water 💧",
    0: "Gun 🔫"
}

computer = random.choice([-1, 0, 1])
print("Computer choice:", choices[computer])

num = int(input("Enter Your Choice (1 Snake 🐍, -1 Water 💧, 0 Gun 🔫): "))

if num not in choices:
    print("Something went wrong!")

elif num == computer:
    print("Its a Draw")

elif (computer == -1 and num == 1):
    print("You Win!")
elif (computer == 1 and num == 0):
    print("You Win!")
elif (computer == 0 and num == -1):
    print("You Win!")