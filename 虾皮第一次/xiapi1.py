#coding=utf-8  
   
import sys  
 
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())  
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n]) 
