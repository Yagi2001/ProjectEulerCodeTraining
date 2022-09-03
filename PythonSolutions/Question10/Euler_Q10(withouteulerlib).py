import time
start_time = time.time()
import math
def is_prime(x):
    is_true = True
    for i in range(2, int(math.sqrt(x)+1)):
        if(x%i==0):
            is_true = False
            break
    return is_true

sum = -1 + 2
for j in range(1,2000000,2):
    if(is_prime(j)):
        sum+=j

print(sum)
print("This took : "+str(time.time()-start_time)+" seconds")

