# (1) 1000 1001
# (2) 第一步进行数学分析 x+y=n x*y=x*(n-x)=nx-x^2 其对称轴 -n/-2 = n/2 故直接取靠近n/2的两个数相加即可
import math


def find_max(number):
    if (number % 2 == 0):
        return [2, 2]
    else:
        return [math.floor(number / 2), math.ceil(number / 2)]


n = input("请输入正整数: ")
n = int(n)
print(find_max(n))
