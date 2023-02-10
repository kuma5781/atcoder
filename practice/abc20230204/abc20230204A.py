N = int(input())
A = [None] * N
B = [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
    print(A[i] + B[i])