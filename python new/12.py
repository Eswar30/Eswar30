# Read a file

# f = open("text.txt", "rt") # rt is default mode [Text mode]
# # content = f.read() 
# # print(content)
# for line in f:
#     print(line)

f = open("eswar.txt", "rt")
# text = f.read()
# print(text)

# for line in f:
#     print(line)

# f.close()
# print(f.readline())
print(f.readlines())
f.close()