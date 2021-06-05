# Lambda functions or Anonymous functions
# Lambda is a one liner functioin not more than that
def add (a, b):
    return a+b
minus = lambda x, y: x+y

print(minus(2,2))
print(add(2,2))

a = [[1, 14], [5,6], [8,23]]

# Sorting using lambda
a.sort(key=lambda x:x[1])
print(a)