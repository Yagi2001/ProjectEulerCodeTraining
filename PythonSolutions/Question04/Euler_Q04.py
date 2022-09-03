def is_palindrome(num):
    str_num = str(num)
    str_num_reversed = str_num[::-1]
    if str_num ==str_num_reversed:
        return  True
max = 0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if is_palindrome(i*j) and i*j>max:
            max = i*j
print(max)
