import math
import random

cnt = 0
N = 1000000
for i in range(N):
    x = random.uniform(2, 3)
    y = random.uniform(0, 21)
    if y <= math.pow(x, 2) + 4 * x * math.sin(x):
        cnt += 1

S = cnt / N * 21
print(S)
