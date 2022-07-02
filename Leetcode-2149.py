nums = list(map(int,input().split()))
num1 = list()
num2 = list()
for i in nums:
    if i>0:
        num1.append(i)
    else:
        num2.append(i)
nums.clear()
for i in range(len(num1)):
    nums.append(num1[i])
    nums.append(num2[i])
print(nums)
    