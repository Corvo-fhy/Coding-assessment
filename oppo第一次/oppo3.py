import sys

# 读取输入
str_num = sys.stdin.readline().strip()
x, y = map(int, sys.stdin.readline().strip().split())

# 计算 x 和 y 的位数
x_num, y_num = len(str(x)), len(str(y))

# 如果字符串长度不够，直接返回 -1
if x_num + y_num > len(str_num):
    print(-1)
    exit()

# 遍历可能的切割位置
for i in range(x_num, len(str_num) - y_num + 1):
    num1, num2 = int(str_num[:i]), int(str_num[i:])  # 直接转换整数
    
    if num1 % x == 0 and num2 % y == 0:
        print(num1, num2)
        exit()

# 如果找不到符合条件的分割点，输出 -1
print(-1)
