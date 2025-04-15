import sys

T = int(sys.stdin.readline().strip())
res = []
for _ in range(T):
    line = sys.stdin.readline().strip()
    n = int(line.split()[0])
    m = int(line.split()[1])
    k = int(line.split()[2])
    if k % 2 ==0:
        threshold = k // 2
    else:
        threshold = k // 2 + 1
    max_1 = (threshold-1)+k
    max_0 = threshold-1
    if max_0 * n >= m:
        res.append(0)
        continue
    res.append((m // max_1))
for s in res:
    print(s)