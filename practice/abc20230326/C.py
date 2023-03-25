import collections

N = int(input())
A = list(map(int, input().split()))
pair = 0
c = collections.Counter(A)
for k in c:
    pair += c[k]//2

ans = 0
for i in range(N // 2):
    if i + 1 > pair:
        break
    ans += 1