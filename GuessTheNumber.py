import random

done = False
lives = 5
print("the goal of this game is to guess a number between one and  twenty, you have 5 trys before game over")
while(done == False):
    randomNumber = random.randint(1,20)
    numberString = input("enter your guess : ")
    number =int(numberString)
    numberValid = False
    while(numberValid == False):
        if(number <= 20 and number >= 1):
            numberValid = True
        elif(number > 20) :
            numberString = input("enter  a valid guess number too high : ")
            number =int(numberString)
        elif (number < 1):
            numberString = input("enter your guess, number is too low : ")
            number =int(numberString)
    
    if(number == randomNumber):
        done = True
        print("Well Done you have guessed succesfully")
    else:
        lives = lives - 1
        if (lives == 0):
            print("game over, you lost.")    
            done = True
        else:
            print("Try again, you have ", lives," left")