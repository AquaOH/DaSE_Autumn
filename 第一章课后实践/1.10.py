a = input("请输入字符串: ")
L = list(a)
length = len(L)
for i in range(1, length):
    if L[i] == L[i - 1]:
        print("含有")
        exit(0)  # 终止运行,括号内表示状态值,默认为0
print("不含有")
