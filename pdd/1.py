import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip()))
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1,n):
        if nums[i] == 0:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + 1
    if max(dp) == 9:
        print("lucky")
    else:
        print("unlucky")