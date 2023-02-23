N = int(input())
T = [None] * N
A = [None] * N
for i in range(N):
    T[i], A[i] = input().split()
    A[i] = int(A[i])

M = 0
for i in range(N):
    if T[i] == "+":
        M += A[i]
    elif T[i] == "-":
        M -= A[i]
    else:
        M *= A[i]

    if M < 0:
        M += 10000
    M %= 10000
    print(M)