import sys

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left-1


T = int(sys.stdin.readline().strip())
res_all = []
for _ in range(T):
    line = sys.stdin.readline().strip()
    n1 = int(line.split()[0])
    n2 = int(line.split()[1])
    if n1 > n2:
        res_all.append('[-1]')
        continue
    elif n1 == n2:
        s1 = list(map(int, sys.stdin.readline().strip()))
        s2 = list(map(int, sys.stdin.readline().strip()))

        s1.sort()
        res = []
        for i in range(n2):
            index = binary_search(s1, s2[i])
            if index == -1:
                res = [-1]
                break
            if s1[index] < s2[i]:
                res.append(s1[index])
                s1.pop(index)
                while s1:
                    res.append(s1[-1])
                    s1.pop()
                break
            res.append(s1[index])
            s1.pop(index)

    else:
        s1 = list(map(int, sys.stdin.readline().strip()))
        s2 = list(map(int, sys.stdin.readline().strip()))

        s1.sort(reverse=True)
        res = f'{s1}'

    res = str(res)
    res_all.append(res)


for res in res_all:
    print(res.replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))