N = int(input())
W = [None] * N
X = [None] * N
for i in range(N):
    W[i], X[i] = map(int, input().split())

ans = 0

# 標準時を一時間ずつずらして、従業員数Wがどれくらい働いているか計算し、その和をamountに入れる
# N個の要素（拠点数）を確認後、amountの最大値をansに入れる
for t in range(24):
    amount = 0
    for j in range(N):
        y = (X[j] + t) % 24 # 一日24時間なので、24で割ったあまりを次の時間としている
        if (9 <= y and y < 18):
            amount += W[j]
    ans = max(ans, amount)

print(ans)

