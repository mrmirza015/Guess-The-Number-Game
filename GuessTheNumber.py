import random
print("Welcome here, This is Number Guessing Game from 1-100")
randNum=random.randint(1,100)
count=0
cond=True
while(cond):
    count=count+1
    you=(int)(input("Enter your Guess:\n"))
    if(randNum==you):
        print(f"You guessed it correcly in {count} turn")
        cond=False
    elif(randNum > you):
        print("Your Guess is slightly lower\n")
        cond=True
    elif(randNum < you):
        print("Your Guess is slightly greater\n")
        cond=True
    
