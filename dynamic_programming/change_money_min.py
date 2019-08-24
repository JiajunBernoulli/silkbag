'''
找零钱问题：所用面额数量最少
跟上面思路相同，代码不同点：
1、填写边界值时，第一行仍是看取余是不是为0，如果为0，填的是除以它的商，即用了几张。
2、填写边界值第一列时，  第一列代表用了这一面额的纸币且剩下的数额为0，代表值用着一种纸币就可以构成这种数额，
用的张数应该填到（i，j）处，所以第一列都是0；
3、写状态转化方程时，要注意判断，如果数额小于面额，直接等于上一层值，dp[i][j]=dp[i-1][j]；  
如果数额等于面额，直接等于1；如果数额大于面额，先判断当用掉一张面额时，
使用当前面额的剩余数额处是否有值，和不使用当前面额的剩余数额处是否有值，
即当dp[i-1][j]!=0&&dp[i][j-num[i]]!=0即这两处都有值，就看那一个更小，如果不都有，仅仅选择一个有值的就好了
'''

nums=[20, 10]
m = len(nums)
target = 60
dp = [[0 for i in range(0, target+1)] for j in range(0, m)]
for j in range(0, target+1):      # 第一行初始化
    if j % nums[0] == 0:
        dp[0][j] = j//nums[0]

for i in range(1, m):
    for j in range(1, target+1):
        if j < nums[i-1]:
            dp[i][j] = dp[i-1][j]
        elif j == nums[i]:
            dp[i][j] = 1
        else:
            if dp[i-1][j] != 0 and dp[i][j-nums[i]] != 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-nums[i-1]]+1)
            else:
                dp[i][j] = dp[i-1][j] if dp[i-1][j] != 0 else dp[i][j-nums[i-1]]
print(dp[m-1][target])