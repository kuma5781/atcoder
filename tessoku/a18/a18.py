N, S = map(int, input().split())
A = list(map(int, input().split()))

# 0からSもしくはNの配列が必要なので配列の要素を+1している
dp = [[None] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(1, S + 1):
    dp[0][i] = False

for i in range(1, N + 1):
    for j in range(S + 1):
        # j - A[i - 1]をするためこの条件分岐が必要
        if j < A[i - 1]:
            if dp[i - 1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        else:
            if dp[i - 1][j] == True or dp[i - 1][j - A[i - 1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S] == True:
    print("Yes")
else:
    print("No")

