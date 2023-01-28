N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = [[None] * 3 for _ in range(Q)]
for i in range(Q):
    query[i] = list(map(int, input().split()))

for i in range(Q):
    if query[i][0] == 2:
        print(A[query[i][1] - 1])
    else:
        A[query[i][1] - 1] = query[i][2]
