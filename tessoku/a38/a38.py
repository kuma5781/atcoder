D, N = map(int, input().split())
L = [None] * N
R = [None] * N
H = [None] * N
for i in range(N):
    L[i], R[i], H[i] = map(int, input().split())

# D日間それぞれの日に最大値の24時間を初期値として設定
LIM = [24] * D

# N回 L, R, Hの呼び出しがあるため N回ループを回す
for i in range(N):
    # LからRまでの最大値を求めるため、L~R回ループを回す
    # 異なるiでも期間がかぶる事があるので、今までの最小値（LIM[j - 1]）と今回の時間内（H[i]）を比較する
    for j in range(L[i], R[i] + 1):
        LIM[j - 1] = min(LIM[j - 1], H[i])

ans = 0
for i in range(D):
    ans += LIM[i]
print(ans)