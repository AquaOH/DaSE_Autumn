a = int(input("请输入数字: "))


def isMersenne(a):
    cnt = 0
    if a == 1 or a == 2:
        print("素数")
        return 0
    for i in range(2, a):
        if a % i == 0:
            cnt = 1
    if cnt == 1:
        print("非素数")
    else:
        print("素数")
    return 0


isMersenne(a)
