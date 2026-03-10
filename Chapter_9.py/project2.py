# The game() function in a program lets a user play a game and return the sore as an integer. you need to read a file 'hi_score.txt' which is either blank or contains the previous hi-score. tou need to write a progam to update the hi-score whenver the game() function breaks the hi.score.

import random
num = random.randint(1, 10)
time = int(input("How many rounds do you want to play? 🎮😊 "))
for i in range (time):
    user = int(input("Which number is in your mind between 1 and 10? 🤔🔢=  "))
    if(num==user):
        print("congratulations you win 🎉")
         
        break
    elif(num!=user):
        print("Try angin")
else:
        print("Time out")