num1 = 20
guess1=9
print("game starts now\nYou have 9 guesses")
while(1):
    guess1 = guess1-1
    userinput = int(input("Guess the number\n"))
    if(userinput < num1):
        print("You entered smaller number\n Try again")
        print("No of guesses left",guess1)
        continue
    if(userinput > num1):
        print("You entered greater number\n Try again")
        print("No of guesses left",guess1)
        continue
    if(guess1 == 0):
        print("Game Over\n Better luck next time")
        continue
    if(userinput == num1):
        print("Cograts you won the game")
        print("whith",9-guess1,"chances")
        break