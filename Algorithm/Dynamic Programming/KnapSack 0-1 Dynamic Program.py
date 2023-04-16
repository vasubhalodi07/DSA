def knapsack(val,wt,W,n):
    if(n==0 or W==0):
        return 0
    if(wt[n-1] > W):
        return knapsack(val, wt, W, n-1)
    else:
        return max(knapsack(val, wt, W, n-1),val[n-1]+knapsack(val, wt, W-wt[n-1], n-1))

val = [60,100,120]
wt = [10,20,40]
W = 50
n = len(val)
print(knapsack(val, wt, W, n))

