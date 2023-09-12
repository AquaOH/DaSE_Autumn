def jiecheng(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * jiecheng(n - 1)


n = input("请输入数字: ")
n = int(n)
print(jiecheng(n))
