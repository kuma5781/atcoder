import collections

N = int(input())
A = list(map(int, input().split()))
pair = 0
c = collections.Counter(A)
# Counterの実装
# dict = {}
# for a in A:
#     if a in dict.keys():
#         dict[a] += 1
#     else:
#         dict[a] = 1
# print(dict)

for k in c:
    pair += c[k]//2

ans = 0
for i in range(N // 2):
    if i + 1 > pair:
        break
    ans += 1