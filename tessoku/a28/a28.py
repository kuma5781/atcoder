N = int(input())
T = [None] * N
A = [None] * N
for i in range(N):
    T[i], A[i] = input().split()
    A[i] = int(A[i])

ans = 0
R = 10000
for i in range(N):
    if T[i] == "+":
        ans += A[i]
    elif T[i] == "-":
        ans -= A[i]
    else:
        ans *= A[i]

    if ans < 0:
        ans += R
    ans %= R
    print(ans)