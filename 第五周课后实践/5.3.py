def InsertSort(list):
    cnt = 0
    length = len(list)
    for i in range(1, length):
        if list[i] < list[i - 1]:
            temp = list[i]
            for j in range(i - 1, -1, -1):
                if temp < list[j]:
                    list[j + 1] = list[j]
                    cnt = j
                    # 最后一次，在最后一个满足temp<a[j]时记录,这个最后的a[j]随后移动一位,故temp需要坐的位置就是这个j
            list[cnt] = temp
    return list


list = [9, 64, 1153, 415, 465, 2, 6, 84, 1, 654]
print(InsertSort(list))
