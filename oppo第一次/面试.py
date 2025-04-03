
def getK(nums, k):
    hashTable = {}
    n = len(nums)
    for i in range(n):
        hashTable[i] = k - nums[i]
    for i in range(n):
        if hashTable[i] in nums:
            return i, nums.index(hashTable[i])
        
print(getK([1,3,4,6,9], 15))

# adam优化器原理
# 连续特征转为离散的好处
# 正则化
# 注意力机制
# 项目细节