import sys

def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i - 1] == False:
            dfs(i - 1, G, visited)

sys.setrecursionlimit(200000)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
if N != M + 1:
    print("No")
    exit()

G = [list() for _ in range(N)]
for a, b in edges:
    G[a - 1].append(b)
    G[b - 1].append(a)

for i in range(N):
    if len(G[i]) > 2:
        print("No")
        exit()

visited = [False] * N
dfs(0, G, visited)

for i in range(N):
    if visited[i] == False:
        print("No")
        exit()

print("Yes")