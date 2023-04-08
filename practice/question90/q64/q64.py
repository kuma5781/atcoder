N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 右隣の区画との差分を求める
B = [None] * N
## 最後の区画は次の区画に行く不便さはないので0を挿入しておく
B[N - 1] = 0
for i in range(N - 1):
    B[i] = A[i + 1] - A[i]
#事前準備したBの不便さの合計値を求める
ans = sum([abs(b) for b in B])

for i in range(Q):
    l, r, v = map(int, input().split())
    # 変化があるのはlの区画とrの区画のみ
    ## l, l + 1間の不便さはlに格納されるのでl - 2の不便さを求める
    ## r, r + 1間の不便さはr - 1に格納されるのでr - 1の不便さを求める
    before = abs(B[l - 2]) + abs(B[r - 1])
    if l - 1 != 0:
        B[l - 2] += v
    if r != N:
        B[r - 1] -= v
    after = abs(B[l - 2]) + abs(B[r - 1])
    ans += after - before
    print(ans)
