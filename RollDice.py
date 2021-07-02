import random

done = False
while(done == False):
    first = random.randint(1,6)
    second = random.randint(1,6)
    print("the number on the first dice is ",first)
    print("the number on the second dice is ",second)
    answer = input(" are you done")
    if(answer == "yes"):
        done =True