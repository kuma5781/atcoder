N, X = map(int, input().split())
A = list(map(int, input().split()))


def search(X, A, N):
    L = 0
    R = N - 1
    while L <= R:
        M = (L + R) // 2
        if X < A[M]:
            R = M - 1
        if X == A[M]:
            return M
        if X > A[M]:
            L = M + 1
    return -1

ans = search(X, A, N)
print(ans + 1)
