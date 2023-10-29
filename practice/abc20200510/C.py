N, M, X = map(int, input().split())

c = []
a = []

for i in range(N):
    C, *A = map(int, input().split())
    c.append(C)
    a.append(A)

ans = 10 ** 9

# bit全探索（選ぶ、選ばない組み合わせはそれぞれ2ケース、これは2進数と同じ原理から最大2**Nまでの数を2進数に変換して、それぞれの桁の値が1であれば選ぶを示すこととして、計算する）
# 1~2**N-1までの数値（0はこの問題では不要）を0~Nビットシフトさせて1が立っていたらその要素が指す、cとAを追加する
# Aの各要素の合計がX以上であれば、その時のCの合計をansと比較して小さい方をansに代入する
for i in range(2 ** N):
    if i == 0:
        continue
    skill = [0] * M
    total_cost = 0
    for j in range(N):
        if ((i >> j) & 1):
            total_cost += c[j]
            for k in range(M):
                skill[k] += a[j][k]
    if min(skill) >= X:
        ans = min(ans, total_cost)

if ans == 10 ** 9:
    print(-1)
else:
    print(ans)

