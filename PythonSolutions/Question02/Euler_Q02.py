num = 1
sum = 0
while(sum<4000000):
    sum_old = sum
    sum = num+sum
    num = sum_old
    if(sum%2==0):
        print(sum)

