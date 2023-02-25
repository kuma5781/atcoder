Q = int(input())
queries = [input().split() for _ in range(Q)]

Map = {}
for i in range(Q):
    if queries[i][0] == "1":
        Map[queries[i][1]] = queries[i][2]
    if queries[i][0] == "2":
        print(Map[queries[i][1]])