import math

str1 = input("请输入IP地址: ")
list1 = str1.split(".")  # 字符串拆解为列表,分割依据是.


def convert_to_bin(str1):  # 输入字符得是数字
    list2 = list()
    cnt = 0
    while str1 != 0:
        list2.append(str(str1 % 2))
        str1 = math.floor(str1 / 2)
        cnt += 1
    while cnt < 8:
        list2.append('0')
        cnt += 1

    list2.reverse()
    str2 = "".join(list2)  # join函数内使用列表,列表内元素得是字符串
    return str2


for elem in list1:
    print(convert_to_bin(int(elem)), end='')
