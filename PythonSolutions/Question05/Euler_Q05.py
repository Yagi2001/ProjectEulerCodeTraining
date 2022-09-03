import math
def is_prime(x):
    is_true = True
    for i in range(2, int(math.sqrt(x)+1)):
        if(x%i==0):
            is_true = False
            break
    return is_true
all_primes_multiplied=1
counter = 0
for i in range(2,21):
    if is_prime(i):
        all_primes_multiplied*=i
for n in range(1,100):
    for j in range(2,21):
        if (n*all_primes_multiplied)%j==0:
            counter+=1
    if(counter==19):
        print(all_primes_multiplied*n)
        break
    counter = 0
