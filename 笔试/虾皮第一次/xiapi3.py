#coding=utf-8  
   
import sys  
 
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    line = line[1:-1]
    nums = list(map(int, line.split(',')))  
    n = len(nums)
    max_price = 0
    max_profit = -1
    for i in range(n-1, -1, -1):
        if nums[i] > max_price:
            max_price = nums[i]
        else:
            max_profit = max(max_profit, max_price - nums[i])
    print(max_profit)