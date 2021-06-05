while(1):
    userinput = int(input("Enter the number grater than 100\n"))
    if userinput<100:
        print("Sorry you enterd the number smaller thean 100\n")
        continue
    if userinput>100:
        print("congrats you entred the number grater thean 100\n")
        break
