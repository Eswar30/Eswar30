#  Dictionary & Its Functions

d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}

print(d2["Rohan"])
d2["Ankit"]  = "Junk food" # to  add an entry 
d2.update({"ankit":"Junk food"}) # to  add an entry
d3  = d2 # now d1 and d2 are  inter connected
del d3["Ankit"] #  ankit will be Deleted from  both d2 and d3

print(d2)
d4  = d2.copy()
print(d4)
