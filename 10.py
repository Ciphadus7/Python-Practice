nums = '10,20,30,40,50'

nums_list = (nums.split(','))
print (nums_list)

nums1 = [int(n) for n in nums_list]
print(nums1)