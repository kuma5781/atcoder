N, K = map(int, input().split())
A = list(map(int, input().split()))

def search(N, K, A):
    L = 1
    R = 10 ** 9
    while L < R:
        M = (L + R) // 2
        sum = 0
        for i in range(N):
            sum += M // A[i]
        if sum < K:
            L = M + 1
        if sum >= K:
            R = M
    return L

ans = search(N, K, A)
print(ans)