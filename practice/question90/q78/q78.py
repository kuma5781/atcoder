N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(N)]
for a, b in edges:
    G[a - 1].append(b)
    G[b - 1].append(a)

ans = 0
for i in range(len(G)):
    cnt = 0
    for j in range(len(G[i])):
        if G[i][j] < i + 1:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)