from collections import deque

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = deque()
for i in range(len(A)):
    S.append(A[i])

# deque()のrotateを使うと、pypyならACできる
# deque()のappnedとpopを使って右シフトしたらもう少し速くできる？
for i in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        x = S[T[1] - 1]
        y = S[T[2] - 1]
        S[T[1] - 1] = y
        S[T[2] - 1] = x
    elif T[0] == 2:
        A = S.rotate(1)
    else:
        print(S[T[1] - 1])