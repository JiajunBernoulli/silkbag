'''
这个文件封装了十大排序算法
'''
# 简单排序
def BubbleSort(array):
    '''
    冒泡排序
    :param array:
    :return:
    '''
    n = len(array)
    if n <= 1:
        return array
    # 第i轮
    for i in range(0, n):
        # 终点受i轮影响，每轮往前减少一次
        for j in range(0, n-i-1):
            # 从小到大排，大的往后换
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] # 交换两数的简易写法
    return array
def SelectSort(lst):
    '''
    选择排序
    :param lst:
    :return:
    '''
    n=len(lst)
    if n<=1:
        return lst
    for i in range(0,n-1):
        minIndex=i
    for j in range(i+1,n):     #比较一遍，记录索引不交换
        if lst[j]<lst[minIndex]:
            minIndex=j
    if minIndex!=i:          #按索引交换
        (lst[minIndex],lst[i])=(lst[i],lst[minIndex])
    return lst
def InsertSort(lst):
    '''
    简单插入排序
    :param lst:
    :return:
    '''
    n=len(lst)
    if n<=1:
        return lst
    for i in range(1,n):
        j=i
        target=lst[i]            #每次循环的一个待插入的数
        while j>0 and target<lst[j-1]:       #比较、后移，给target腾位置
            lst[j]=lst[j-1]
            j=j-1
        lst[j]=target            #把target插到空位
    return lst
# 复杂排序
def QuickSort(lst):
    '''
    快速排序
    :param lst:
    :return:
    '''
    # 此函数完成分区操作
    def partition(arr, left, right):
        key = left  # 划分参考数索引,默认为第一个数为基准数，可优化
        while left < right:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1
            # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left += 1
            # 此时已找到一个比基准大的书，和一个比基准小的数，将他们互换位置
            (arr[left], arr[right]) = (arr[right], arr[left])

        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
        (arr[left], arr[key]) = (arr[key], arr[left])
        # 返回目前基准所在位置的索引
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return
        # 从基准开始分区
        mid = partition(arr, left, right)
        # 递归调用
        # print(arr)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(lst)
    if n <= 1:
        return lst
    quicksort(lst, 0, n - 1)
    return lst
def ShellSort(lst):
    '''
    希尔排序
    :param lst:
    :return:
    '''
    def shellinsert(arr,d):
        n=len(arr)
        for i in range(d,n):
            j=i-d
            temp=arr[i]             #记录要出入的数
            while(j>=0 and arr[j]>temp):    #从后向前，找打比其小的数的位置
                arr[j+d]=arr[j]                 #向后挪动
                j-=d
            if j!=i-d:
                arr[j+d]=temp
    n=len(lst)
    if n<=1:
        return lst
    d=n//2
    while d>=1:
        shellinsert(lst,d)
        d=d//2
    return lst
def  HeapSort(lst):
    '''
    堆排序
    :param lst:
    :return:
    '''
    def heapadjust(arr,start,end):  #将以start为根节点的堆调整为大顶堆
        temp=arr[start]
        son=2*start+1
        while son<=end:
            if son<end and arr[son]<arr[son+1]:  #找出左右孩子节点较大的
                son+=1
            if temp>=arr[son]:       #判断是否为大顶堆
                break
            arr[start]=arr[son]     #子节点上移
            start=son                     #继续向下比较
            son=2*son+1
        arr[start]=temp             #将原堆顶插入正确位置
#######
    n=len(lst)
    if n<=1:
        return lst
    #建立大顶堆
    root=n//2-1    #最后一个非叶节点（完全二叉树中）
    while(root>=0):
        heapadjust(lst,root,n-1)
        root-=1
    #掐掉堆顶后调整堆
    i=n-1
    while(i>=0):
        (lst[0],lst[i])=(lst[i],lst[0])  #将大顶堆堆顶数放到最后
        heapadjust(lst,0,i-1)    #调整剩余数组成的堆
        i-=1
    return lst

def MergeSort(lst):
    '''
    归并排序
    :param lst:
    :return:
    '''
    # 合并左右子序列函数
    def merge(arr, left, mid, right):
        temp = []  # 中间数组
        i = left  # 左段子序列起始
        j = mid + 1  # 右段子序列起始
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for i in range(left, right + 1):  # !注意这里，不能直接arr=temp,他俩大小都不一定一样
            arr[i] = temp[i - left]

    # 递归调用归并排序
    def mSort(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mSort(arr, left, mid)
        mSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    n = len(lst)
    if n <= 1:
        return lst
    mSort(lst, 0, n - 1)
    return lst

# 线性时间非比较排序
def CountSort(lst):
    '''
    计数排序
    :param lst:
    :return:
    '''
    n=len(lst)
    num=max(lst)
    count=[0]*(num+1)
    for i in range(0,n):
        count[lst[i]]+=1
    arr=[]
    for i in range(0,num+1):
        for j in range(0,count[i]):
            arr.append(i)
    return arr
def BucketSort(lst):
    '''
    桶排序
    :param lst:
    :return:
    '''
    ##############桶内使用快速排序
    def QuickSort(lst):
        def partition(arr, left, right):
            key = left  # 划分参考数索引,默认为第一个数，可优化
            while left < right:
                while left < right and arr[right] >= arr[key]:
                    right -= 1
                while left < right and arr[left] <= arr[key]:
                    left += 1
                (arr[left], arr[right]) = (arr[right], arr[left])
            (arr[left], arr[key]) = (arr[key], arr[left])
            return left

        def quicksort(arr, left, right):  # 递归调用
            if left >= right:
                return
            mid = partition(arr, left, right)
            quicksort(arr, left, mid - 1)
            quicksort(arr, mid + 1, right)

        # 主函数
        n = len(lst)
        if n <= 1:
            return lst
        quicksort(lst, 0, n - 1)
        return lst

    ######################
    n = len(lst)
    big = max(lst)
    num = big // 10 + 1
    bucket = []
    buckets = [[] for i in range(0, num)]
    for i in lst:
        buckets[i // 10].append(i)  # 划分桶
    for i in buckets:  # 桶内排序
        bucket = QuickSort(i)
    arr = []
    for i in buckets:
        if isinstance(i, list):
            for j in i:
                arr.append(j)
        else:
            arr.append(i)
    for i in range(0, n):
        lst[i] = arr[i]
    return lst
def RadixSort(lst):
    '''
    基数排序
    :param lst:
    :return:
    '''
    import math
    def getbit(x,i):       #返回x的第i位（从右向左，个位为0）数值
        y=x//pow(10,i)
        z=y%10
        return z
    def CountSort(lst):
        n=len(lst)
        num=max(lst)
        count=[0]*(num+1)
        for i in range(0,n):
            count[lst[i]]+=1
        arr=[]
        for i in range(0,num+1):
            for j in range(0,count[i]):
                arr.append(i)
        return arr
    Max=max(lst)
    for k in range(0,int(math.log10(Max))+1):             #对k位数排k次,每次按某一位来排
        arr=[[] for i in range(0,10)]
        for i in lst:                 #将ls（待排数列）中每个数按某一位分类（0-9共10类）存到arr[][]二维数组（列表）中
            arr[getbit(i,k)].append(i)
        for i in range(0,10):         #对arr[]中每一类（一个列表）  按计数排序排好
            if len(arr[i])>0:
                arr[i]=CountSort(arr[i])
        j=9
        n=len(lst)
        for i in range(0,n):     #顺序输出arr[][]中数到ls中，即按第k位排好
            while len(arr[j])==0:
                j-=1
            else:
                lst[n-1-i]=arr[j].pop()
    return lst

if __name__ == '__main__':
    array = [5, 4, 3, 2, 1]
    print(BubbleSort(array))
    print(SelectSort(array))
    print(InsertSort(array))

    print(ShellSort(array))
    print(HeapSort(array))
    print(QuickSort(array))

    print(MergeSort(array))

    print(CountSort(array))
    print(BucketSort(array))
    print(RadixSort(array))



