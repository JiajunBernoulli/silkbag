'''
带价值的背包问题
有 n 个重量和价值分别为Wi,Vi的物品，现从这些物品中挑选出总量不超过 W 的物品，求所有方案中价值总和的最大值。
Sample Input:
3 4
1 2
2 5
3 7
Sample Output:
9
'''
weights = [1, 2, 3]
values = [2, 5, 7]
capacity = 4
n = len(weights)
dp = [[0 for i in range(0, n+1+1)] for j in range(0, capacity+1+1)]
for i in range(1, n+1):
    for j in range(1, capacity+1):
        # weights和value中的i-1才是第i个
        if(j>=weights[i-1]):
            # 剩余空间放得下，取放下或者不放下的最大值
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+values[i-1])
        else:
            # 放不下直接同于前一个
            dp[i][j]=dp[i-1][j]
print(dp[n][capacity])