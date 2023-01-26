N = int(input())
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
Q = int(input())
A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

S = [[0] * 1501 for _ in range(1501)]
for i in range(N):
    S[X[i]][Y[i]] += 1

T = [[0] * 1501 for _ in range(1501)]
for y in range(1, 1501):
    for x in range(1, 1501):
        T[x][y] = T[x - 1][y] + S[x][y]

for x in range(1, 1501):
    for y in range(1, 1501):
        T[x][y] = T[x][y - 1] + T[x][y]

for i in range(Q):
    print(T[C[i]][D[i]] + T[A[i] - 1][B[i] - 1] - T[A[i] - 1][D[i]] - T[C[i]][B[i] - 1])



