N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None] * N
# 部屋1の最短経路をdp[0]として考える
dp[0] = 0
dp[1] = A[0]

# 動的計画法
for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

print(dp[N - 1])


# 部屋1の最短経路をdp[1]として考える
dp = [None] * N + 1
dp[1] = 0
dp[2] = A[0]

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i - 2], dp[i - 2] + B[i - 3])

print(dp[N])