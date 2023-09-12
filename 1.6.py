a = input("输入第一个数: ")
b = input("输入第二个数: ")
c = input("输入第三个数: ")
d = input("输入第四个数: ")
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if a > d:
    a, d = d, a
if b > c:
    b, c = c, b
if b > d:
    b, d = d, b
if c > d:
    c, d = d, c
print(a, b, c, d)
