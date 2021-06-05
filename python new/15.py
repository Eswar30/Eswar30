# Global varaible / Local variable
# Global varaiable will be printed when there is no local variable

l = 10 # Global

def functiion1(n):
    # l = 5 # Local
    m = 8 # Local 
    global l
    l = l + 45
    print(l,m)  # It prints l as 5 because l = 5 is a local varable 
    print(n,"I have printed")

print(l)
functiion1("This is me")
x = 89
# Nasted function: A function inside a function
def harry():
    x = 20
    def rohan():
        global x 
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)
harry()
print(x)

    