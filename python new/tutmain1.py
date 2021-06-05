# __name__ = __main__

def printf(string):
    return f"Ye string harry  ko de de thakur {string}"
def add(num1 , num2):
    return num1 + num2 +5 # Wrong addition

print("and the name is", __name__) # The value of name is main only when it is exicuted in same file

if __name__ == '__main__': # This will ignored when it is imported
    print(printf("Harry")) # It works only in this file
    o = add(4,6)
    print(o)