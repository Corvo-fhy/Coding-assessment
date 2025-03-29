import sys

T = int(sys.stdin.readline().strip())
res = ["" for _ in range(T)]
for t in range(T):
    line = sys.stdin.readline().strip()
    temp = list(map(int, line.split()))
    n, k = temp[0], temp[1]
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    sums = sum(a)
    max_work = n * k
    if max_work - sums >= 0:
        res[t] = "YES"
    else:
        res[t] = "NO"
for i in range(T):
    print(res[i])
