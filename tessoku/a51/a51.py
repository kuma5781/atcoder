from collections import deque

Q = int(input())
queries = [input().split() for _ in range(Q)]

S = deque()

for i in range(Q):
    if queries[i][0] == "1":
        S.append(queries[i][1])
    if queries[i][0] == "2":
        print(S[-1])
    if queries[i][0] == "3":
        S.pop()