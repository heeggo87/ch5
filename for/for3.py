nums = [5,9,3,8,2]
max = nums[0]

for n in nums:
    if max < n:
        max = n

print('최대값:', max)