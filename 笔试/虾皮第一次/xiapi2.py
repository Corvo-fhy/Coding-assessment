#coding=utf-8  
   
import sys  
 
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  
    left = 0
    right = n
    while right - left > 1e-6:
        mid = (left + right) / 2
        if mid * mid < n:
            left = mid
        else:
            right = mid
    print(round(left, 3))