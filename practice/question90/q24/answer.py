N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = 0
for i in range(N):
    d += abs(A[i] - B[i])

# Kが操作回数、dが最低限必要な操作回数（実質は差分の大きさ）なのでK>=dを満たす必要がある
if K >= d and (K - d) % 2 == 0:
    print("Yes")
else:
    print("No")