import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [None] * Q
A.sort()

for i in range(Q):
    B[i] = int(input())
    index = bisect.bisect(A, B[i])
    if index == 0:
        print(abs(A[0] - B[i]))
    elif index == N:
        print(abs(A[len(A) - 1] - B[i]))
    else:
        print(min(abs(A[index - 1] - B[i]), abs(A[index] - B[i])))
