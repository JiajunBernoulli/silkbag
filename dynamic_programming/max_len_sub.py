'''
数组最大不连续递增子序列长度
arr[] = {3,1,4,1,5,9,2,6,5}的最长递增子序列长度为4。即为：1,4,5,9

设置一个数组temp，长度为原数组长度，数组第i个位置上的数字代表0...i上最长递增子序列，
当增加一个数字时，最大递增子序列可能变成前面最大的递增子序列+1，
也可能就是前面最大递增子序列，这需要让新增加进来的数字arr[i]跟前面所有数字比较大小，
    即当 arr[i] > arr[j]，temp[i] = max{temp[j]}+1，其中，j 的取值范围为：0,1...i-1，
    当 arr[i] < arr[j]，temp[i] = max{temp[j]}，j 的取值范围为：0,1...i-1，
所以在状态转换方程为temp[i]=max{temp[i-1], temp[i-1]+1}
'''
# n=int(input())
array = [1, 1, 2, 1, 3, 4, 2, 4, 3]
n=len(array)
# for i in range(0,n):
#     num=int(input())
#     array.append(num)
temp = [1 for i in range(0,n)]
for i in range(1, n):          # 终点
    for j in range(0, i):      #
        print("arr[j]:"+str(array[j])+"arr[i]:"+str(array[i]))
        if array[i]>array[j] and temp[j]+1>temp[i]:
            temp[i] = temp[j] + 1
            print("temp:", end="")
            print(temp)
    print("--------")
print(max(temp))

print("=====")
thisMax=max(temp)
for j in range(n-1, -1, -1):
    if temp[j] == thisMax:
        print(array[j])
        thisMax-=1
'''
[1, 1, 2, 1, 3, 4, 2, 4, 3]
4 

[1, 1, 2, 1, 2, 3, 2, 3, 3]
3
'''