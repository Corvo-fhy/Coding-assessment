import sys
import time

# 超时
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
# start = time.time()
mat = [[0 for _ in range(n-1)] for _ in range(n)]

for i in range(n):
    mat[i] = values[0:i] + values[i+1:n]
minimum = float('inf')
for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(0, n-2, 2):
        sum1 += mat[i][j]
        sum2 += mat[i][j+1]
    if j+2 < n-1:
        sum1 += mat[i][j+2]
    minimum = min(minimum, abs(sum1-sum2))
# end = time.time()
# print("Time taken:", end - start)
print(minimum)