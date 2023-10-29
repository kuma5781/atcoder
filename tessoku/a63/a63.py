from collections import deque

# N, M = map(int, input().split())
# edges = [list(map(int, input().split())) for _ in range(M)]

# G = [list() for _ in range(N)]
# for a, b in edges:
#     G[a - 1].append(b)
#     G[b - 1].append(a)

# # 幅優先探索の初期化
# dist = [-1] * N
# dist[0] = 0
# Q = deque()
# Q.append(1)

# # 幅優先探索
# while len(Q) > 0:
#     pos = Q.popleft()
#     for nex in G[pos - 1]:
#         if dist[nex - 1] == -1:
#             dist[nex - 1] = dist[pos - 1] + 1
#             Q.append(nex)

# for i in range(N):
#     print(dist[i])


# 要素を直感的に書くと以下のようになる
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 要素数を直感的にするために、0番目の要素は使わないが、それを含めてN+1個用意する
G = [list() for _ in range(N + 1)]

for a, b in edges:
    G[a].append(b)
    G[b].append(a)

# distは頂点1からの距離を表す。初期値は-1。探索してヒットしたらその距離を適切な要素に記録する。
dist = [-1] * (N + 1) # 要素0番目の値は実質使わないが直感的に示すためにN+1個用意する
dist[1] = 0
Q = deque()
Q.append(1)

# 幅優先探索
while len(Q) > 0:
    pos = Q.popleft()
    # 頂点posに隣接する頂点nexについて、nexが未探索であれば、頂点1からの距離（dist）に頂点posからの距離（dist[pos]）に1を足したものを代入する。
    # その後、nexを探索済みとしてキューに追加する。
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            Q.append(nex)

for i in range(1, N + 1):
    print(dist[i])