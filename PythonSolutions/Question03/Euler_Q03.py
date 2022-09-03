import math
def is_prime(x):
    is_true = True
    for i in range(2, int(math.sqrt(x)+1)):
        if(x%i==0):
            is_true = False
            break
    return is_true
number = 600851475143
for x in range(2,10000):
    if (number%x==0 and is_prime(x)==True):
            if(number/x!=1):
                number/=x
for n in range(int(number),1,-1):
    if number%n==0 and is_prime(n)==True:
        print(n)
        break





