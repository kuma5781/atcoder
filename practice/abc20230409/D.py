A, B = map(int, input().split())
cnt = 0
while A != B:
    A, B = max(A, B), min(A, B)
    if A % B == 0:
        cnt += A // B - 1
        A = B
    else:
        cnt += A // B
        A = A % B

print(cnt)