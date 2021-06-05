# Exercise 4
"""
pattern printing
input = intefer n where n = no of rows
boolean =
True
*
**
***
****

False
****
***
**
*

"""
userinput1 = bool(int(input("Enter 0 for False and any other number for True\n")))
userinput2 = int(input("Enter the number of rows:  "))
print("You Have choose", userinput1)
if(userinput1 == True):
    for i in range(userinput2):
        for j in range(i+1):
            print("*", end="")
        print()
    # for j in range(1,userinput2+1):
    #     print("*" * j)
else:
    for i in range(userinput2):
        for j in range(userinput2-i):
            print("*", end="")
        print()

