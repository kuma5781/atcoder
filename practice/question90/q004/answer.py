H, W = map(int, input().split())
A = [[None] * W for _ in range(H)]

for i in range(H):
    A[i] = list(map(int, input().split()))

AH = [0] * H
AW = [0] * W

for i in range(H):
    for j in range(W):
        AH[i] += A[i][j]

for i in range(W):
    for j in range(H):
        AW[i] += A[j][i]

N = [[None] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        N[i][j] = AH[i] + AW[j] - A[i][j]

for i in range(H):
    print(" ".join(str(j) for j in N[i]))
