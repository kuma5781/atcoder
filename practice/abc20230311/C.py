H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = [0]
visited = set()

# 全探索を再帰関数で求める
# 各returnは再帰関数の中の1つの関数に対して行っている。
# 一つ一つreturnすることで大元の呼び出し関数に戻る。
def dfs(i, j, visited):
    if A[i][j] in visited:
        return
    if i == H - 1 and j == W - 1:
        ans[0] += 1
        return
    visited.add(A[i][j])
    if j + 1 < W:
        dfs(i, j + 1, visited)
    if i + 1 < H:
        dfs(i + 1, j, visited)
    visited.remove(A[i][j])

dfs(0, 0, visited)
print(ans[0])
