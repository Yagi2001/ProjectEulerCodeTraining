import eulerlib as eul
sum = 0
for i in eul.primes(1999999):
    sum+=i
print(sum)
