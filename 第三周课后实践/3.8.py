import math
import random
import time


def bubble_sort(arry):
    n = len(arry)  # 获得数组的长度
    for i in range(n):
        for j in range(1, n - i):  # 每轮找到最大数值 或者用 for j in range(i+1, n)
            if arry[j - 1] > arry[j]:  # 如果前者比后者大
                arry[j - 1], arry[j] = arry[j], arry[j - 1]  # 则交换两者
    return arry


# 插入排序
def insert_sort(ary):
    count = len(ary)
    for i in range(1, count):
        key = i - 1
        mark = ary[i]  # 注： 必须将ary[i]赋值为mark，不能直接用ary[i]
        while key >= 0 and ary[key] > mark:
            ary[key + 1] = ary[key]
            key -= 1
        ary[key + 1] = mark
    return ary


def heap_sort(ary):
    n = len(ary)
    first = int(n / 2 - 1)  # 最后一个非叶子节点
    for start in range(first, -1, -1):  # 构建最大堆
        max_heapify(ary, start, n - 1)
    for end in range(n - 1, 0, -1):  # 堆排，将最大跟堆转换成有序数组
        ary[end], ary[0] = ary[0], ary[end]  # 将根节点元素与最后叶子节点进行互换，取出最大根节点元素，对剩余节点重新构建最大堆
        max_heapify(ary, 0, end - 1)  # 因为end上面取的是n-1，故而这里直接放end-1，相当于忽略了最后最大根节点元素ary[n-1]
    return ary


# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
# start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary, start, end):
    root = start
    while True:
        child = root * 2 + 1  # 调整节点的子节点
        if child > end:
            break
        if child + 1 <= end and ary[child] < ary[child + 1]:
            child = child + 1  # 取较大的子节点
        if ary[root] < ary[child]:  # 较大的子节点成为父节点
            ary[root], ary[child] = ary[child], ary[root]  # 交换
            root = child
        else:
            break


def create_chaos(l, a, b):
    n = random.randint(a, b)
    for i in range(n):
        l.append(math.floor(random.random() * 1000))


def run_time(l):
    T1 = time.perf_counter()
    bubble_sort(l)
    T2 = time.perf_counter()
    print("冒泡排序的耗时为:%s毫秒" % ((T2 - T1) * 1000))
    T3 = time.perf_counter()
    insert_sort(l)
    T4 = time.perf_counter()
    print("插入排序的耗时为:%s毫秒" % ((T4 - T3) * 1000))
    T5 = time.perf_counter()
    heap_sort(l)
    T6 = time.perf_counter()
    print("堆排序的耗时为:%s毫秒" % ((T6 - T5) * 1000))


l1 = list()
l2 = list()
l3 = list()
create_chaos(l1, 10, 100)
create_chaos(l2, 100, 1000)
create_chaos(l3, 1000, 10000)

run_time(l1)
run_time(l2)
run_time(l3)

print("在样本量较小情况下,长度越长,冒泡排序受影响最大,堆排序其次,插入排序受影响最小")
