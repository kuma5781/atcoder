from itertools import accumulate

N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [None] * Q
R = [None] * Q
for q in range(Q):
    L[q], R[q] = map(int, input().split())

# 累積和の計算
S = list(accumulate([0] + A))

for q in range(Q):
    print(S[R[q]] - S[L[q] - 1])