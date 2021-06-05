'''
Exercise 2 - Faulty Calculator
Design a calculator which will correctly solve all the problems except
the following ones:
45 * 3 = 555, 56+9 = 77, 56/6 = 4
Your program should take operator  and the two numbers as input from the user
and then return the result
'''
print("select operator\n + for addition\n - for subtraction\n x for multiplication\n / for division")
op= input()
print("Enter first number")
no1= int(input())
print("Enter second number")
no2= int(input())
if op == "+" and no1 == 56 and no2 == 9:
    print("The sum of two numbers is")
    print(77)
elif op == "x" and no1 == 45 and no2 == 3:
    print("The multiplication of two numbers is")
    print(555)
elif op == "/" and no1 == 56 and no2 == 6:
    print("The division of two numbers is")
    print(4)
elif op == "+":
    print("The sum of two numbers is")
    print(int(no1+no2))
elif op == "-":
    print("The subtraction of two numbers is")
    print(int(no1-no2))
elif op == "x":
    print("The multiplication of two numbers is")-
    print(int(no1*no2))
elif op == "/":
    print("The division of two numbers is")
    print(int(no1/no2))
else:
    print("Choose the correct operator as menctioned above")