# N = int(input())
# S = [None] * N
# for i in range(N):
#     S[i] = input()

# A = [False] * N
# T = []

# for i in range(N):
# ここで計算量O(N)かかっている
#     if S[i] in T:
#         continue
#     else:
#         T.append(S[i])
#         A[i] = True

# 無駄な処理
# 上段で出力できる
# for i in range(N):
#     if A[i]:
#         print(i + 1)

N = int(input())
S = [None] * N
for i in range(N):
    S[i] = input()

T = set()

for i in range(N):
    if S[i] not in T:
        T.add(S[i])
        print(i + 1)