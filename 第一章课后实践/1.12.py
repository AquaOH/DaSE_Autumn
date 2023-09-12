import math


def find_3gen(n):
    temp = n
    minf = 0
    highc = n
    while abs(n - math.pow(temp, 3)) >= math.pow(10, -5):
        if math.pow(temp, 3) > n:
            highc = temp
            temp = (temp + minf) / 2
        else:
            minf = temp
            temp = (temp + highc) / 2
    return temp


n = input("请输入待求三次方根的数: ")
n = float(n)
if n < 0:
    print(-find_3gen(-n))
else:
    print(find_3gen(n))
