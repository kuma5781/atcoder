N, K = map(int,input().split())
S = [None] * K
for i in range(K):
    S[i] = input()
S.sort()
for i in range(K):
    print(S[i])