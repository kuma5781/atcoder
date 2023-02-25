from collections import deque

Q = int(input())
queries = [input().split() for _ in range(Q)]

T = deque()

for i in range(Q):
    if queries[i][0] == "1":
        T.append(queries[i][1])
    if queries[i][0] == "2":
        print(T[0])
    if queries[i][0] == "3":
        T.popleft()