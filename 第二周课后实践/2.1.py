
# (2) 第一步进行数学分析 x+y=n x*y=x*(n-x)=nx-x^2 其对称轴 -n/-2 = n/2 故直接取靠近n/2的两个数相加即可
import math


def find_max(number, l):
    if number == 2:
        l.append(2)
        return 2
    elif number == 3:
        l.append(3)
        return 3
    elif number % 2 == 0:
        return find_max(number / 2, l) , find_max(number / 2, l)
    else:
        return find_max(math.floor(number / 2), l) , find_max(math.ceil(number / 2), l)

l1 = []
find_max(2001,l1)
print("(1)",l1)
print("(2)第一步进行数学分析 x+y=n x*y=x*(n-x)=nx-x^2 其对称轴 -n/-2 = n/2 故直接取靠近n/2的两个数相加即可，只要再不停分下去，指数增长就很快")

n = input("(3)请输入正整数: ")
n = int(n)
l = []
find_max(n, l)
print(l)
