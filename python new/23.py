# ============map function===========
number = ["3","34","64"]
number = list(map(int, number))

# for i in range(len(number)):
#     number[i] = int(number[i])

number[2] = number[2]+1
print(number[2])


def sq(a):
    return a*a
num= [2,3,5,6,76,3,3,2]
square = list(map(sq, num))
print(square)
# Using lambda insteard of creating a function
square = list(map(lambda a: a*a, num))
print(square)


def square1(a):
    return a*a
def cube(a):
    return a*a*a
func = [square1,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)

# =============Filter=============
list_1 = [1,2,3,4,5,6,7,8,9]

def is_grater_5(num):
    return num>5

gr_than_5 = list(filter(is_grater_5,list_1))
print(gr_than_5)


# =============Reduce==============

from functools import reduce
list_2 = [1,2,3,4]

num1 = reduce(lambda x,y:x+y, list_2)
print(num1)

