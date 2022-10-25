numbers = list(range(1500, 3201))
nums = list()

for n in numbers:
    if n % 7 == 0 and n % 5 != 0:
        nums.append(str(n))
    
print(','.join(nums))
