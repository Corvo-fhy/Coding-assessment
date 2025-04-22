# 给定一个数字X，求最大的y，使得y满足：
# y * ⌈y/2⌉ * ⌊y/3⌋ ≤X
import math

def f(y):
    return y * ((y+1)//2) * (y//3)

def find_max_y(x):
    left, right = 0, x  # 假设一个合理的上界，具体值可以根据需要调整
    result = 0
    if x == 1:
        return 2
    
    while left <= right:
        mid = (left + right) // 2
        if f(mid) <= x:
            result = mid  # 找到一个满足条件的 y
            left = mid + 1  # 尝试更大的 y
        else:
            right = mid - 1  # 尝试更小的 y
    
    return result

print(find_max_y(35))
print(find_max_y(36))

# print((1//3))