import sys


def getMax(dicts):
    max = 0
    for i in dicts:
        if dicts[i][-1] > dicts.get(max, [0])[-1]:
            max = i
    return max

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
n = values[0]
m = values[1]
line = sys.stdin.readline().strip()
priceses = list(map(int, line.split()))
priceses.sort()
qu = {}
for i in range(m):
    line = sys.stdin.readline().strip()
    values=(list(map(int, line.split())))
    if values[0] in qu:
        stack = []
        while len(qu[values[0]]) != 0 and qu[values[0]][-1] > values[1]:
            stack.append(qu[values[0]].pop())
        qu[values[0]].append(values[1])
        qu[values[0]].extend(stack)
    else:
        qu[values[0]] = [values[1]]
res = 0
while priceses and qu:
    max = getMax(qu)
    find = False
    for i in range(n):
        if priceses[i] >= max:
            find = True
            break
    if find:
        res += qu[max].pop()
        priceses.pop(i)
        n = n - 1
        if len(qu[max]) == 0:
            del qu[max]
    else:
        break
print(res)