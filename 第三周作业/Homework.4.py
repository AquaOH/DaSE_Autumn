import random
import math

s = 1 * 21
N = 100000000
C = 0
for i in range(N):
    x = random.uniform(2, 3)
    y = random.uniform(0, 21)
    if y <= (math.pow(x, 2) + 4 * x * math.sin(x)):
        C += 1
I = C / N * s
print(I)
