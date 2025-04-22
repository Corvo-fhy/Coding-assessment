import sys

n = int(sys.stdin.readline().strip())
values = list(map(int, sys.stdin.readline().strip().split()))

# 计算前缀和
prefix_even = [0] * (n + 1)  # 偶数索引前缀和
prefix_odd = [0] * (n + 1)   # 奇数索引前缀和

for i in range(n):
    prefix_even[i + 1] = prefix_even[i] + (values[i] if i % 2 == 0 else 0)
    prefix_odd[i + 1] = prefix_odd[i] + (values[i] if i % 2 == 1 else 0)

# 原始的 A 和 B 的和
sum_even = prefix_even[n]   # A 取偶数索引和
sum_odd = prefix_odd[n]     # B 取奇数索引和

minimum = float('inf')

# 遍历删除每个元素 i
for i in range(n):
    if i % 2 == 0:
        # 删除偶数索引，A/B 角色对调
        new_sum_even = prefix_odd[i] + (sum_even - prefix_even[i + 1])
        new_sum_odd = prefix_even[i] + (sum_odd - prefix_odd[i + 1])
    else:
        # 删除奇数索引，A/B 角色对调
        new_sum_even = prefix_even[i] + (sum_odd - prefix_odd[i + 1])
        new_sum_odd = prefix_odd[i] + (sum_even - prefix_even[i + 1])

    minimum = min(minimum, abs(new_sum_even - new_sum_odd))

print(minimum)
