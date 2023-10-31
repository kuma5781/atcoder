import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

a_sorted = sorted(A)

ans = 0
for i in range(N):
    right = bisect.bisect_left(a_sorted, a_sorted[i] + M)
    ans = max(ans, right - i)
print(ans)
