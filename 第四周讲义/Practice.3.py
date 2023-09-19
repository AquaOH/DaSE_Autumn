# Python数据结构——栈Stack
"""前置:python中的class"""


class MyTestClass:
    def __init__(self):  # __init__在类被实例化后会自动调用,即自动执行函数里的数据
        print("我被自动调用了")

    def prt(self):
        print(self)
        print(self.__class__)

    def prt1(runoob):
        print(runoob)
        print(runoob.__class__)


"""__class__功能和type()函数一样，都是查看对象所在的类"""

x = MyTestClass()
x.prt()
x.prt1()
"""
self代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
"""

print("\n现在开始实现一个栈\n")


# 以下开始实现一个栈
class Stack():
    def __init__(self):
        self.__items = []

    def size(self):
        return len(self.__items)

    def isempty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.__items.append(element)  # 压栈

    def pop(self):
        try:
            return self.__items.pop()
        except:
            print("ERROR: Stack is empty now!")

    def peek(self):
        try:
            return self.__items[-1]
        except:
            print("ERROR: Stack is empty now!")


s = Stack()
s.push(1)
print(s.pop())
print(s.pop())
print("**********")
s.push(3.5)
s.push(2.7)
print(s.peek())
print(s.size())
print(s.isempty())
