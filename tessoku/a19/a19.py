N, W = map(int, input().split())
w = [None] * N
v = [None] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[-10 ** 15] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(W + 1):
        if j < w[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            # -∞としておくことで存在しない重さの組み合わせを最大値として取らないようにする
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

print(max(dp[N]))