# 查看变量类型

num_1 = 6
num_2 = 3.14
num_3 = "Tom"
list_1 = [1, 2, 3, 4, 5]
dict_1 = {'a': 1, 'b': 2, 'c': 3}
print(type(num_1))
print(type(num_2))
print(type(num_3))
print(type(list_1))
print(type(dict_1))

# 查看变量地址

print(id(num_1))
print(id(num_2))
print(id(num_3))
print(id(list_1))
print(id(dict_1))

# 判断对象类型

a = 2
print(isinstance(a, int))  # a是不是int,是返回True
b = [1, 2, 3]
print(isinstance(b, tuple)) # b是不是tuple,不是返回False
