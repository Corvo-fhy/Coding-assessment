import sys


# 有部分样例无法通过
n = int(sys.stdin.readline().strip())
if n == 1:
    print(2)
else:
    while True:
        res = n
        if n % 2 == 0:
            n = n + 1
            continue
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                n = n + 1
                break
        if res == n:
            print(n)
            break