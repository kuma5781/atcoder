mod = 998244353
N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0, 0] for _ in range(N)]
dp[0] = [1, 1]

# 一手前の選び方をもとに今のカードの選び方を算出する
# 隣合う2枚のカードで選び方は全部で4通り。そのため2件、2件の全検索を行っている
# 一手前の表のカードと今の表のカードが異なる場合、今のカードの選び方に足す
for i in range(1, N):
    for pre in range(2):
        for nxt in range(2):
            if data[i - 1][pre] != data[i][nxt]:
                dp[i][nxt] += dp[i - 1][pre]
    dp[i][0] %= mod
    dp[i][1] %= mod

print((dp[N - 1][0] + dp[N - 1][1]) % mod)