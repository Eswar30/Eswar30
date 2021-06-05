# *args and **kwargs

# def functoin_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
# functoin_name_print("Harry", "Rohan","Skillf","Hammad", "Shivam")

# args
def funargs(normal ,*args, **kwargs):
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key}is a{value}")
har = ["Harry", "Rohan","Skillf","Hammad", "Shivam"]
funargs(*har)
normal = "Iam a normal argument and the students are:"

kw = {"Rohan":"Moniter","Harry":"Fitness Trainer"}
