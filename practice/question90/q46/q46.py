N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Ax = [0] * 46
Bx = [0] * 46
Cx = [0] * 46

# 準備段階で各要素を46で割った余りを求め、その個数メモする
for a in A:
    x = a % 46
    Ax[x] += 1
for b in B:
    x = b % 46
    Bx[x] += 1
for c in C:
    x = c % 46
    Cx[x] += 1

cnt = 0
# A, B, Cのそれぞれの要素の和を46で割った余りが0の場合、それぞれの要素の個数分カウントする（積で求める）。
# O(46**3)なので間に合う。問題文通りに書いたらO(N**3)になるので、間に合わない。
for a, i in enumerate(Ax):
    for b, j in enumerate(Bx):
        for c, k in enumerate(Cx):
            if (a + b + c) % 46 == 0:
                cnt += i * j * k

print(cnt)