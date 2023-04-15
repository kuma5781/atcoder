N = int(input())
A = list(map(int, input().split()))

# Aの要素の和が10で割り切ればい場合、"No"を出力して、プログラムを終了する
if sum(A) % 10 != 0:
    print("No")
    exit()

# Aの要素の累積和を求める
cumsum = [0]
for i in range(N):
    cumsum.append(cumsum[i] + A[i])

# 累積和の最後の要素を取得
last = cumsum[-1]

# 累積和の配列をsetに変換する
cumsum_set = set(cumsum)
print(cumsum_set)

# 条件に当てはまる累積和が存在するか調べる
for x in cumsum_set:
    if (x + last // 10) % last in cumsum_set:
        print('Yes')
        exit()

print('No')