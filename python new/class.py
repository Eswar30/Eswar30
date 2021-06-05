# Average
n= int(input("For how many numbers you want to average\n"))
i=0
sum1 = list()
while(i<n):
    num = int(input("Enter no of cases\n"))
    i = i+1
    sum1.append(float(num))

ave = sum(sum1)/len(sum1)
print("The average of the numbers is\n", ave)