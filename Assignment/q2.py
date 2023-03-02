nums = [100, 2, 300, 10, 11, 1000]

largest_number = nums[0]

for number in nums:
    if number > largest_number:
        largest_number = number

print(largest_number)