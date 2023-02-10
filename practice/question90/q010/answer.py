N = int(input())
C = [None] * N
P = [None] * N

for i in range(N):
    C[i], P[i] = map(int, input().split())

print(C)
print(P)

# C1とC2を別々の配列にしたいために、条件分岐で1 or 0を作り、1 or 0との積を取っている。
is_1 = [1 if (x==1) else 0 for x in C]
is_2 = [1 if (x==2) else 0 for x in C]
P1 = [x*y for x,y in zip(P,is_1)]
P2 = [x*y for x,y in zip(P,is_2)]

print(P1)
print(P2)

# 累積和の0番目の要素には必ず0を入れる。そうしないと1番目の要素の増加分が求められない。その分配列の要素数も1大きくなる。
S1 = [0] * (N + 1)
S2 = [0] * (N + 1)
for i in range(1, N + 1):
    S1[i] = S1[i - 1] + P1[i - 1]

for i in range(1, N + 1):
    S2[i] = S2[i - 1] + P2[i - 1]

print(S1)
print(S2)

Q = int(input())
L = [0] * Q
R = [0] * Q
for i in range(Q):
    L, R = map(int, input().split())
    print(f"{S1[R] - S1[L - 1]} {S2[R] - S2[L - 1]}")
