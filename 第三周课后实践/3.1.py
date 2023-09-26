import math
def ten2bin(N,l):
    if N == 0:
        return 0
    else:
        l.append(N%2)
        return ten2bin(math.floor(N/2),l)


l=[]
N= int(input("请输入数字: "))
ten2bin(N,l)
for i in range(len(l)):
    print(l.pop(),end='')