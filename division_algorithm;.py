# 辗转相除法
a=input()
b=input()
def func(a,b):
    if a<b:
        a, b=b, a
    r = a%b
    while(r!=0):
        a=b
        b=r
        r=a%b
    return b
print(func(int(a), int(b)))
