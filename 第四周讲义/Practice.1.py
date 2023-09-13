import math

"""
a = input("请输入IP地址")

list1 = a.split(".")
for i in range(len(list1)):
    print(bin(int(list1[i])),end='')
"""


L = "11001010011110000101011100001100"
list2 = list(L)
list3 = list()
for i in range(4):
    sum41 = 0
    for j in range(8 * i, 8 * i + 8):
        sum41 += math.pow(2,8*i+7-j)*int(list2[j])
    list3.append(str(int(sum41)))
str1 = ".".join(list3)
print(str1)


