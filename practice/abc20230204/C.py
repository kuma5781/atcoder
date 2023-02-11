import sys

def dfs(pos, G):
    visited[pos] = True
    for i in G[pos]:
        if visited[i - 1] == False:
            dfs(i - 1, G)

sys.setrecursionlimit(200000)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(N)]
for a, b in edges:
    G[a - 1].append(b)
    G[b - 1].append(a)

# 連結成分の個数を求める
visited = [False] * N
cnt = 0
for i in range(N):
    if(visited[i] == False):
        dfs(i, G)
        cnt += 1

print(M - N + cnt)
