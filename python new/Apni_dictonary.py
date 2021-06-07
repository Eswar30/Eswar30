# Create a dictonary and take input from the user and return the meaning of the word form the dictionary
d1= {"Variable": "Storage containers  or memory location to  store values",
     "Comment" : "comments  are  used to explain python  code",
     "Integer" : "Integer  is  nothing but numbers",
     "Float" :"The  decimal  values are known as floting ",
     "Typecasting" : "The casting is a   pricess of converting one type to another"
    }
userinput1= input("Enter the word\n")
print("Definition: ",d1[userinput1])

