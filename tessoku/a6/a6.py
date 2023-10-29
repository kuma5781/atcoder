N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [None] * Q
R = [None] * Q
for q in range(Q):
    L[q], R[q] = map(int, input().split())

# 累積和の計算
S = [None] * (N + 1)
S[0] = 0
for i in range(N):
    S[i + 1] = S[i] + A[i]

for q in range(Q):
    print(S[R[q]] - S[L[q] - 1])