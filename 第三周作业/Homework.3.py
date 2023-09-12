a = [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2]


def findcoin(l):
    all_coins = len(a)
    highc = all_coins - 1
    minf = 0
    while (114):
        if all_coins % 2 != 0:
            left = highc
            highc = highc - 1
        mid = int((minf + highc - 1) / 2)
        sum_l = 0
        sum_r = 0
        for i in range(minf, mid + 1):
            sum_l += a[i]
        for j in range(mid + 1, highc + 1):
            sum_r += a[j]
        if sum_l < sum_r:
            highc = mid
        if sum_l > sum_r:
            minf = mid + 1
        if sum_l == sum_r:
            return left
        if minf + 1 == highc:
            if a[minf] < a[highc]:
                return minf
            else:
                return highc


print(findcoin(a))
