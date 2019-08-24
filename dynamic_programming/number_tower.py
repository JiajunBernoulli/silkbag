
'''
数塔问题
解决方案是自底至顶分析，自上而下计算。因此我们从第四层的四个数据开始分析：

如果最优路径经过2，那么一定经过19
如果最优路径经过18，那么一定经过10
如果最优路径经过9，那么一定经过10
如果最优路径经过5，那么一定经过16

因此，我们总结出规律：如果最有路径经过当前点，那么从当前点到路径尾节点的数字之和将是当前点的值加上左右孩子其中较大的值，即：
martix[i][j] += max(martix[i+1][j], martix[i+1][j+1])
'''
# martix = [
#     [7],
#     [3, 8],
#     [8, 1, 0],
#     [2, 7, 4, 4],
#     [4, 5, 2, 6, 5],
# ]  ## 答案30
martix = [
            [9],
            [12, 15],
            [10, 6, 8],
            [2, 18, 9, 5],
            [19, 7, 10, 4, 16]
] # 答案59
n=len(martix)
for i in range(n-2, -1, -1):
    for j in range(len(martix[i])):
        martix[i][j] += max(martix[i+1][j], martix[i+1][j+1])
print(martix[0][0])