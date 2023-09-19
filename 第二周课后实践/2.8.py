import math
import random


def monte_carlo():
    N = 1000000
    cnt = 0
    for i in range(N):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (math.pow(x - 1 / 2, 2) + math.pow(y - 1 / 2, 2)) < 1 / 4:
            cnt += 1

    pi = (cnt / N * 1 * 4)
    print("{:.10f}".format(pi))


def find_pi1():
    N = 1000000
    sum = 0
    for i in range(N):
        sum += math.pow(-1, i) * (1 / (2 * i + 1))
    print("{:.10f}".format(sum * 4))


def find_pi2():
    N = 1000000
    sum = 0
    for i in range(N):
        sum += 1 / math.pow(i + 1, 2)
    pi = math.pow(6*sum,1/2)
    print("{:.10f}".format(pi))


monte_carlo()
find_pi1()
find_pi2()
