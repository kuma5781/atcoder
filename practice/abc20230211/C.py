from collections import deque
import itertools

N, M = map(int, input().split())
C = [None] * M
A = [list() for _ in range(M)]
for i in range(M):
    C[i] = int(input())
    A[i].extend(list(map(int, input().split())))

ans = 0
for i in range(1 << len(A)):
    combination = []
    for j in range(len(A)):
        if ((i >> j) & 1):
            combination.append(A[j])
    check = deque([False] * (N + 1))
    for i in range(1, N + 1):
        if i in set(itertools.chain.from_iterable(combination)):
            check[i] = True
    check.popleft()
    if all(check):
        ans += 1

print(ans)
