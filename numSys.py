def decimalism2Other(n,k):
    '''
    十进制转换为其他进制(0-16)，除k取余法
    :param n:  待转换的十进制数
    :param k:   目标进制
    :return:    转换后数对应的字符串
    '''
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
    b = []
    while True:
        s = n // k  # 商
        y = n % k  # 余数
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    return "".join(map(str, b))

def other2Decimalism(numStr, k):
    '''
    任意进制转十进制，按权展开法
    :param numStr:  待转换数的字符串
    :param k:       待转换数的进制
    :return:        十进制结果
    '''
    length = len(numStr)
    res = 0
    for i in range(length):
        t=k**(length-1-i)*int(numStr[i])
        res += t
    return res
print(decimalism2Other(520, 2))
print(other2Decimalism("1000001000", 2))