from collections import deque
from statistics import mean

N = int(input())
S = deque()
X = list(map(int, input().split()))
X.sort()
for i in range(len(X)):
    S.append(X[i])

for i in range(N):
    S.popleft()
    S.pop()