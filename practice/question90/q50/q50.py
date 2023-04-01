N, L = map(int, input().split())

mod = 10 ** 9 + 7

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

# 動的計画法を用いて、i番目の要素に到達する方法の数を求める
for i in range(2, N + 1):
    if i - L >= 0:
        dp[i] = dp[i - 1] + dp[i - L]
    else:
        dp[i] = dp[i - 1]

print(dp[N]%mod)