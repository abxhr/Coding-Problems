# Author: Abshar Mohammed Aslam, github.com/abxhr

string = input()
nums = [int(i) for i in string.strip('[]').split(',')]
s = 0
string = "["
for i in range(len(nums)):
    nums[i] += s
    s = nums[i]
    string += str(nums[i]) + ","
string = string[:-1] + "]"
print(string)
