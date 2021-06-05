# F strings
import math

me = "Harry"
a1 =3
b = "this is %s %s"%(me, a1)
c = "This is {1} {0}"
d = c.format(me, a1)
print(b)
a = f"This is {me} {a1}  {math.sin(0)}"
print(a)

