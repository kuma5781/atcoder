# 完答できていない
# N = int(input())
# A = [None] * N
# B = [None] * N
# C = [None] * N
# D = [None] * N

# Z = [[0] * 1501 for _ in 1501]
# for i in range(N):
#     Z[A[i]][B[i]] += 1
#     Z[C[i] + 1][D[i] + 1] += 1
#     Z[A[i]][D[i] + 1] -= 1
#     Z[C[i] + 1][B[i]] -= 1

# for y in range(0, 1501):
#     for x in range(1, 1501):
#         T[x][y] = T[x - 1][y] + Z[x][y]
