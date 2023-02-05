import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

# 深さ優先探索
## visitedの引数は無しでも可
def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i - 1] == False:
            dfs(i - 1, G, visited)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(N)]
for a, b in edges:
    G[a - 1].append(b)
    G[b - 1].append(a)

visited = [False] * N
dfs(0, G, visited)

ans = True
for i in range(N):
    if visited[i] == False:
        ans = False
        break

if ans == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")