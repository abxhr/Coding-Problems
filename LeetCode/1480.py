string = input()
nums = [int(i) for i in string.strip('[]').split(',')]
s = 0
for i in range(len(nums)):
    nums[i] += s
    s = nums[i]
print(nums)