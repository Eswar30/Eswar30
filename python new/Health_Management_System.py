# Exercise 5

# Health Management System
# 3 clients - Harry, Rohan and Hammad

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client
"""
We have to create:
3 files for exercise and
3 files for food they eat
for total 6 clients
"""
from datetime import time
from os import read
from typing import Text


def getdate():
    import datetime 
    return datetime.datetime.now()

a = int(input("Select the option:\n 1 for log\n 2 for retrieve\n"))
# if a == 1:
def log():
        c = int(input("Select:\n   1 for Harry\n   2 for Rohan\n   3 for Hammad\n"))
        if c == 1:
            a = int(input("Harry What do you want to choose\n   1 for exerxcise and\n   2 for dite\n"))
            if a == 1:
                x= input("Enter The Exercise\n")
                with open("Harryex.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + x + "\n")
                    print("Added sucessfully")
            elif a == 2:
                x= input("Enter The Dite\n")
                with open("Harrydite.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + x + "\n")
                print("Added sucessfully")
            else:
                print("Please Enter a valid input")
        elif c ==2:
            a = int(input("Rohan What do you want to choose\n   1 for exerxcise and\n   2 for dite\n"))
            if a == 1:
                x= input("Enter The Exercise\n")
                with open("Harryex.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + x + "\n")
                print("Added sucessfully")
            elif a == 2:
                x= input("Enter The Dite\n")
                with open("Harryex.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + x + "\n")
                print("Added sucessfully")
            else:
                print("Please Enter a valid input")

        elif c ==3:
            a = int(input("Hammad What do you want to choose\n   1 for exerxcise and\n   2 for dite\n"))
            if a == 1:
                x= input("Enter The Exercise\n")
                with open("Harryex.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + x + "\n")
                print("Added sucessfully")
            elif a == 2:
                x= input("Enter The Dite\n")
                with open("Harryex.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + x + "\n")
                print("Added sucessfully")
            else:
                print("Please Enter a valid input")

# elif a == 2:
def retrive():
        c = int(input("Select:\n   1 for Harry\n   2 for Rohan\n   3 for Hammad\n"))
        if c == 1:
            a = int(input("Harry What do you want to choose\n   1 for exerxcise and\n   2 for dite\n"))
            if a == 1:
                with open("Harryex.txt") as f:
                    a = f.read()
                    print(a)    
            elif a ==2:
                with open("Harrydite.txt") as f:
                    a = f.read()
                    print(a)                 
                # f= open("Harrydite.txt")
                # print(f)
            else:
                print("Please Enter a valid input")
        elif c ==2:
            a = int(input("Rohan What do you want to choose\n   1 for exerxcise and\n   2 for dite\n"))
            if a == 1:
                with open("Harryex.txt") as f:
                    a = f.read()
                    print(a)
                # f= open("Rohanex.txt")
                # print(f)
            elif a ==2:
                f= open("Rohandite.txt")
                print(f)
            else:
                print("Please Enter a valid input")
        elif c ==3:
            a = int(input("Hammad What do you want to choose\n   1 for exerxcise and\n   2 for dite\n"))
            if a == 1:
                with open("Harryex.txt") as f:
                    a = f.read()
                    print(a) 
                # f= open("Hammadex.txt")
                # print(f)
            elif a ==2:
                with open("Harryex.txt") as f:
                    a = f.read()
                    print(a) 
                # f= open("Hammaddite.txt")
                # print(f)
            else:
                print("Please Enter a valid input")
        else:
            print("Please Enter a valid input")

if a == 1:
    log()
elif a == 2:
    retrive()
else:
    print("Please Enter a valid input")
