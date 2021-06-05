# File Writing

f = open("eswar.txt", "a")
f.write("Harry bahi bahut acche hain\n")

f.close()

# Handle Read and write both [r+ mode]

f= open("eswar.txt", "r+") 
print(f.read())

# more on python files

print(f.readline())
f.seek(0)
print(f.readline())
print(f.readline())
print(f.tell())
f.close()