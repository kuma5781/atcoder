H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

# それぞれのマスでAとBの差分を取り、その差分をAに加算する
# 右端と下端の差分は埋めることができないので、加算することなくAとBが一致していることが条件
ans = 0
for i in range(H):
    for j in range(W):
        if i == H - 1 or j == W - 1:
            if A[i][j] != B[i][j]:
                print("No")
                exit()
        if A[i][j] != B[i][j]:
            tmpSum = B[i][j] - A[i][j]
            A[i][j] += tmpSum
            A[i][j + 1] += tmpSum
            A[i + 1][j] += tmpSum
            A[i + 1][j + 1] += tmpSum
            ans += abs(tmpSum)

print("Yes")
print(ans)