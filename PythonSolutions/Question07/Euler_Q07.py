import math
def is_prime(x):
    is_true = True
    for i in range(2, int(math.sqrt(x)+1)):
        if(x%i==0):
            is_true = False
            break
    return is_true
i = 0
j=1
while i<10001:
    if is_prime(j):
        i+=1
    j+=2
print(j-2)


