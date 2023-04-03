# import itertools
# import math

# 積の計算でO(6**N)
# N回和を求めるので、O((6**N)+N)
# N = int(input())
# A = [list(map(int, input().split())) for _ in range(N)]
# mod = 10**9 + 7

# li = [*map(list, itertools.product(*A))]
# S = 0
# for i in range(len(li)):
#     S += (math.prod(li[i])) % mod

# print(S % mod)


# 一回のsumでO(6)
# それをN回繰り返すのでO(N*6)
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
S = 1
mod = 10**9 + 7
for i in range(N):
    S *= sum(A[i]) % mod
    S %= mod

print(S)