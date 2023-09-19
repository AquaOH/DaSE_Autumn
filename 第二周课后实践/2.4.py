import math

c = float(input("请输入数字: "))
h = float(input("请输入精度: "))
g = 0
while math.pow(g, 2) > c or c > math.pow(g + 1, 2):
    g += 1
while math.fabs(pow(g, 2) - c) > h:
    g += h
print(g)
