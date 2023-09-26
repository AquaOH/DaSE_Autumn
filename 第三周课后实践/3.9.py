import math
import random


def create_blist(list_a, list_b):
    for i in range(len(list_a)):
        list_b.append(multipy_but_except_you(list_a, i))
    return 0


def multipy_but_except_you(list_a, i):
    temp_a = 1
    temp_b = 1
    for m in range(i):
        temp_a *= list_a[m]
    for n in range(i + 1, len(list_a)):
        temp_b *= list_a[n]
    return temp_a * temp_b


def create_chaos(l, a, b):
    n = random.randint(a, b)
    for i in range(n):
        l.append(math.floor(random.random() * 1000))


list_a = [1,2,3,4]
#list_a = []
list_b = []
#create_chaos(list_a, 10, 100)
create_blist(list_a, list_b)
print(list_a)
print(list_b)
