from collections import deque

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(N)]
for a, b in edges:
    G[a - 1].append(b)
    G[b - 1].append(a)

# 幅優先探索の初期化
dist = [-1] * N
dist[0] = 0
Q = deque()
Q.append(1)

# 幅優先探索
while len(Q) > 0:
    pos = Q.popleft()
    for nex in G[pos - 1]:
        if dist[nex - 1] == -1:
            dist[nex - 1] = dist[pos - 1] + 1
            Q.append(nex)

for i in range(N):
    print(dist[i])