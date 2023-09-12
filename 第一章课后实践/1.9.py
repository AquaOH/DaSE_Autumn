n = input("请输入 数列大小: ")
n = int(n)
L = list()
for i in range(n):
    temp = input("请输入第%s个数据: " % (i+1))
    L.append(temp)
for i in range(n - 1, -1, -1):
    print(L[i], end=' ')
