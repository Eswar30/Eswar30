import tutmain1

print("and the name is", __name__) # The value of name is main only when it is exicuted in same file
# Here __name__ is not equals to main because it imported from some where
print(tutmain1.add(5,5))