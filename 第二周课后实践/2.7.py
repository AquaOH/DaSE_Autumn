import math

c = float(input("请输入数字: "))
h = float(input("请输入精度: "))
g = c/2
cnt = 0
while math.fabs(math.pow(g, 3) - c) > h:
    g = (2*g + c / math.pow(g,2)) / 3
    cnt += 1
print(g)
print(cnt)
# 无影响