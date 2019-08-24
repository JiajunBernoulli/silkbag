'''
输入格式：
输入第一行给出一个字符，如果是 C 就表示下面的字符串需要被压缩；如果是 D 就表示下面的字符串需要被解压。
第二行给出需要被压缩或解压的不超过1000个字符的字符串，以回车结尾。题目保证字符重复个数在整型范围内，且输出文件不超过1MB。
输出格式：
根据要求压缩或解压字符串，并在一行中输出结果。

输入样例 1：
C
TTTTThhiiiis isssss a   tesssst CAaaa as
输出样例 1：
5T2h4is i5s a3 te4st CA3a as
输入样例 2：
D
5T2h4is i5s a3 te4st CA3a as10Z
输出样例 2：
TTTTThhiiiis isssss a   tesssst CAaaa asZZZZZZZZZZ
'''

def compress(text):
    i = 0
    while i < len(text)-1:
        j = i+1
        while text[j] == text[i]:
            j += 1
        if j - i > 1:
            print(j-i, end="")
        print(text[i], end="")
        i=j-1
        i+=1
    if i==len(text)-1:
        print(text[i], end="")

def extract(text):
    i=0
    while i < len(text):
        if text[i].isdigit():
            num=int(text[i])
            while text[i+1].isdigit():
                i += 1
                num = num*10+int(text[i])
            for j in range(0, num):
                print(text[i+1], end="")
            i += 1
        else:
            print(text[i], end="")
        i += 1


ch=input()
text=input()
if ch=='C':
    compress(text)
else:
    extract(text)