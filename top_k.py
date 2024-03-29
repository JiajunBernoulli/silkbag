def  HeapSort(lst, k):
    '''
    用堆排序的思想求k个最大的数
    :param lst:
    :param k:
    :return: 返回一个列表，最后k位数字为topk且有序，之前无序
    '''
    def heapadjust(arr, start, end):  # 将以start为根节点的堆调整为大顶堆
        temp = arr[start]
        # 二叉树编号为1~n，比列表索引大1
        son = 2 * start + 1
        while son <= end:
            if son < end and arr[son] < arr[son + 1]:  # 找出左右孩子节点较大的
                son += 1
            if temp >= arr[son]:  # 判断是否为大顶堆
                break

            arr[start] = arr[son]  # 子节点上移
            start = son  # 继续向下比较
            son = 2 * son + 1

        arr[start] = temp  # 将原堆顶插入正确位置
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
    while(i>=n-k):
        (lst[0],lst[i])=(lst[i],lst[0])  #将大顶堆堆顶数放到最后
        heapadjust(lst,0,i-1)    #调整剩余数组成的堆
        i-=1
    print(lst[i+1]) # 打印第k大
    return lst

print(HeapSort([5,2,0,1,3], 2))