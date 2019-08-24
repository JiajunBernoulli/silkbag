'''
数组最大连续子序列和
如arr[] = {6,-1,3,-4,-6,9,2,-2,5}的最大连续子序列和为14。即为：9,2,-2,5

创建一个数组a，长度为原数组长度，不同位置数字a[i]代表0...i上最大连续子序列和，
a[0]=arr[0]设置一个最大值max，初始值为数组中的第一个数字。
当进来一个新的数字arr[i+1]时，判断到他前面数字子序列和a[i]+arr[i+1]跟arr[i+1]哪个大，
前者大就保留前者，后者大就说明前面连续数字加起来都不如后者一个新进来的数字大，前面数字就可以舍弃，
从arr[i+1]开始，每次比较完都跟max比较一下，最后的max就是最大值。

'''
arr = [6, -1, 3, -4, -6, 9, 2, -2, 5]
n=len(arr)
thisMax=arr[0]
thisSum=arr[0]
for i in range(1, n):
    # thisSum=max(thisSum+arr[i], arr[i])  # 等价的简化写法
    # 如果和已经为负数，可以丢弃之前累积的，重新记录和
    if thisSum < 0:
        thisSum=arr[i]
    # 如果和还是正数可以接着累积
    else:
        thisSum += arr[i]
    # 记录出现的连续子串之和的最大值
    if thisSum >= thisMax:
        thisMax = thisSum
print(thisMax)
