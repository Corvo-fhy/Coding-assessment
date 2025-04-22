import sys

res = [0 for _ in range(31)]
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
nums = list(map(int, line.split()))
dp = [0 for _ in range(max(nums) + 1)]
dp[1] = 1
dp[2] = 1
for i in range(3, max(nums) + 1):
    if i % 2 == 0:
        dp[i] = dp[i // 2]
        continue
    for j in range(i - 1, 0, -1):
        if dp[j] == 1:
            break
    dp[i] = 1 + dp[i - j]
print(dp)
for num in nums:
    for i in range(dp[num], min(30, num)):
        res[i] += 1

for i in range(1, 31):
    print(res[i], end=" ")