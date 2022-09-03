import math
for a in range(2,335):
    for b in range(3,500):
        if(b>a):
            c_squared = a**2 + b**2
            c = math.sqrt(c_squared)
            if c.is_integer() and a+b+c == 1000:
                print(a*b*c)

