N, M = map(int, input().split())
S = [None] * N

for i in range(N):
    S[i] = input()

res = 0
for i in range(N):
    for i2 in range(i + 1, N):
        flg = True
        for j in range(M):
            if S[i][j] == "x" and S[i2][j] == "x":
                flg = False
                break
        if flg:
            res += 1
print(res)
