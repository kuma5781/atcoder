N, M = map(int, input().split())
S = [None] * N
T = [None] * M

for i in range(N):
    S[i] = input()
    S[i] = S[i][3:6]
    S[i] = int(S[i])

for i in range(M):
    T[i] = int(input())

cnt = 0
for i in range(N):
    for j in range(M):
        if S[i] == T[j]:
            cnt += 1
            break

print(cnt)