import random
import math

N = int(input("Enter the size of random numbers to be produced : "))
D_plus = []
D_minus = []
_random = []

# Rank the N random numbers
for i in range(0, N):
    _random.append(random.random())
    _random.sort()

# Calculate max(i/N-Ri)
for i in range(1, N + 1):
    x = i / N - _random[i - 1]
    D_plus.append(x)

# Calculate max(Ri-((i-1)/N))
for i in range(1, N + 1):
    y = (i - 1) / N
    y = _random[i - 1] - y
    D_minus.append(y)
560
# Calculate max(D+, D-)
ans = max(int(math.sqrt(N)) * D_plus, int(math.sqrt(N)) * D_minus)
print("Value of D is :")
print(ans)