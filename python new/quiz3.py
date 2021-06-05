list1 =  [ "eswar", 1,2,3,4,5,8,7,9,10,22,255]
for item in list1:
    if str(item).isnumeric() and item>=6:
#    if item.isnumeric() and  item>6:
        print(item)