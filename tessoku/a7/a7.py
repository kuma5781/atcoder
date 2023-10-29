D = int(input())
N = int(input())
L = [None] * N
R = [None] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

# 前日比との比較のリストを作成する
## D+2個の要素を用意しているのは、以下の2点の理由がある
### 1日目の前日比の計算で使用するため、先頭要素には0を設定する
### -1する終了日の要素は終了日の翌日に設定する必要があるため
S = [0] * (D + 2)
for i in range(N):
    S[L[i]] += 1
    S[R[i] + 1] -= 1

# 累積和の計算
## ansのリストには0日目から最終日までの要素を設定するするため、D+1の要素数が必要
ans = [None] * (D + 1)
## 1日目の計算に使用するため、先頭要素には0を設定する
ans[0] = 0
for i in range(1, D + 1):
    ans[i] = ans[i - 1] + S[i]
    print(ans[i])