def find_my_max_division(x, y):
    if (y > x):  # 保证x>y
        temp = x
        x = y
        y = temp
    while (True):
        temp = x % y
        if temp == 0:
            return y
        else:
            x = y
            y = x % y


x = int(input("请输入x: "))
y = int(input("请输入y: "))
print(find_my_max_division(x,y))
