x = input("输入第一个数: ")
y = input("输入第二个数: ")
z = input("输入第三个数: ")
#   x and y  如果第一个为False，输出False，否则输出y的值
#   x or y  如果第一个为True，输出True,否则输出y的值
#   not x 如果x为True,返回False，为False，返回True

if x > y:
    temp = x
    x = y
    y = temp
if x > z:
    temp = x
    x = z
    z = temp
if y > z:
    temp = y
    y = z
    z = temp

print(x, y, z)
