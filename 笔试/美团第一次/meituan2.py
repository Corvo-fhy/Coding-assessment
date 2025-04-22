import sys
import numpy as np

T = int(sys.stdin.readline().strip())
nums = [(0,0) for _ in range(T)]
for t in range(T):
    line = sys.stdin.readline().strip()
    nums[t] = tuple(map(float, line.split()))
n =  int(sys.stdin.readline().strip())
A = np.zeros((T, n+1), dtype=float)
for i in range(T):
    for j in range(n+1):
        A[i][j] = (nums[i][0]) ** j
B = np.zeros((T, 1), dtype=float)
for i in range(T):
    B[i][0] = nums[i][1]
X = np.linalg.lstsq(A, B, rcond=1)[0]
X = np.round(X, 4)
res = ""
# print(len(X))
for i in range(len(X)-1, -1, -1):
    res += str(X[i][0]) + " "
print(res)
