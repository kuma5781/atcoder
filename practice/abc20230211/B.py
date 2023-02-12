import sys

sys.setrecursionlimit(200000)

def dfs(pos, G, visited):
    visited[pos] = True
    tmp.append(pos + 1)
    for i in G[pos]:
        if visited[i - 1] == False:
            dfs(i - 1, G, visited)

N, M = map(int, input().split())
if M == 0:
    ans = []
    for i in range(N):
        ans.append(i + 1)
    print(*ans)
else:
    A = list(map(int, input().split()))
    edges = [None] * len(A)
    for i in range(len(A)):
        edges[i] = [A[i], A[i] + 1]

    G = [list() for _ in range(N)]
    for a, b in edges:
        G[a - 1].append(b)
        G[b - 1].append(a)

    ans = []
    visited = [False] * N
    for i in range(N):
        if visited[i] == False:
            tmp = []
            dfs(i, G, visited)
            tmp.reverse()
            ans.extend(tmp)

    print(*ans)