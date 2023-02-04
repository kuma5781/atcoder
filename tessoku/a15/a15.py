import bisect

N = int(input())
A = list(map(int, input().split()))

T = list(set(A))
T.sort()

B = [None] * N
for i in range(N):
    B[i] = bisect.bisect_left(T, A[i])
    B[i] += 1

ans = " ".join(map(str, B))
print(ans)
