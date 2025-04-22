# 数组的权重问题：有两个数组A，B，定义数组的权重为如果b_i>a_i，则res+=b_i
# 问如何将B数组重新排列，使得数组的权重最大


def find_bigger(A_i, sorted_B):
    left, right = 0, len(sorted_B) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_B[mid] <= A_i:
            left = mid + 1
        else:
            right = mid - 1
    return left  # 返回的是第一个大于A_i的元素的位置

def reorder_B(A, B):
    # 对B进行排序
    sorted_B = sorted(B)
    
    # 创建一个结果数组用于存储重新排序后的B
    reordered_B = [None] * len(A)
    
    # 对A的每个元素进行处理
    for i in range(len(A)):
        idx = find_bigger(A[i], sorted_B)
        
        # 如果找到了比A[i]大的元素
        if idx < len(sorted_B):
            reordered_B[i] = sorted_B[idx]
            # 从sorted_B中移除该元素
            sorted_B.pop(idx)
        else:
            # 如果没有找到大于A[i]的元素，选择B中剩余的最小元素
            reordered_B[i] = sorted_B.pop(0)
    
    return reordered_B

# 示例
A = [1, 3, 2, 4, 5]
B = [6, 7, 8, 9, 10]
reordered_B = reorder_B(A, B)
print("Reordered B:", reordered_B)
