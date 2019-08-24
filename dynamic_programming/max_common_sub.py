'''
两个字符串最大公共子序列
比如字符串1：BDCABA；字符串2：ABCBDAB，则这两个字符串的最长公共子序列长度为4，最长公共子序列是：BCBA
具体思想：设 X=(x1,x2,.....xn)和 Y={y1,y2,.....ym} 是两个序列，将 X 和 Y 的最长公共子序列记为LCS(X,Y)，
如果 xn=ym，即X的最后一个元素与Y的最后一个元素相同，这说明该元素一定位于公共子序列中。
因此，现在只需要找：LCS(Xn-1，Ym-1)就好，LCS(X,Y)=LCS(Xn-1，Ym-1)+1；如果xn != ym，
这下要麻烦一点，因为它产生了两个子问题：LCS(Xn-1，Ym) 和 LCS(Xn，Ym-1)。

动态规划解法：先创建一个解空间即数组，因为给定的是两个字符串即两个一维数组存储的数据，
所以要创建一个二维数组，设字符串X有n个值，字符串Y有m个值，需要创建一个m+1*n+1的二维数组，
二维数组每个位置（i，j）代表当长度为i的X子串与长度为j的Y的子串他们的最长公共子串，
之所以要多创建一个是为了将边界值填入进去，边界值就是第一行跟第一列，指X长度为0或者Y长度为0时，自然需要填0，
其他位置填数字时，当这两个位置数字相同，dp[i][j] = dp[i-1][j-1]+1；当这两个位置数字不相同时，
dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j])。最后二维数组最右下角的值就是最大子串。
'''
str1="BDCABA"
str2="ABCBDAB"
m=len(str1)
n=len(str2)
dp = [[0 for i in range(0, m+1+1)] for j in range(0, n+1+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        # 如果当前末尾子序列相等，那么就为前一个+1
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        # 否则为两者中大的一个
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[m][n])