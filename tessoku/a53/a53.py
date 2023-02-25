import heapq

Q = int(input())
queries = [input().split() for _ in range(Q)]

T = []
for i in range(Q):
    if queries[i][0] == "1":
        heapq.heappush(T, int(queries[i][1]))
    if queries[i][0] == "2":
        print(T[0])
    if queries[i][0] == "3":
        heapq.heappop(T)