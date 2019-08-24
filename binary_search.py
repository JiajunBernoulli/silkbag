def circulationBinarySearch(a, num):
    '''
    循环实现二分查找算法
    :param a:
    :param num:
    :return:
    '''
    length = len(a)
    low = 0
    high = length - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if a[mid] < num:
            low = mid + 1
        elif a[mid] > num:
            high = mid - 1
        else:
            return mid
    return -1

def recursionBinarySearch(ls, num, lower=0, upper=None):
    '''
    递归二分查找算法
    :param ls:
    :param num:
    :param lower:
    :param upper:
    :return:
    '''
    if upper is None:
        upper = len(ls) - 1
    mid = (lower + upper) // 2
    if mid == 0 and num != ls[0]:
        return -1
    if mid == len(ls) - 1 and num != ls[-1]:
        return -1
    if num == ls[mid]:
        return mid
    elif num < ls[mid]:
        return recursionBinarySearch(ls, num, lower, mid)
    else:
        return recursionBinarySearch(ls, num, mid + 1, upper)

print(circulationBinarySearch([5, 8, 9, 12, 17, 19, 20, 22], 9))
print(recursionBinarySearch([5, 8, 9, 12, 17, 19, 20, 22], 9))
