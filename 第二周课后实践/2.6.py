import math

c = float(input("请输入数字: "))
h = float(input("请输入精度: "))
g = c/4
cnt = 0
while math.fabs(math.pow(g, 2) - c) > h:
    g = (g + c / g) / 2
    cnt += 1
print(g)
print(cnt)
# 无影响