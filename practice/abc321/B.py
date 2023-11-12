N, X = map(int, input().split())
A = list(map(int, input().split()))

sorted_A = sorted(A)
sum = 0
for i in range(1, len(sorted_A) - 1):
    sum += sorted_A[i]

if X - sum > sorted_A[-1]:
    print(-1)
    exit()
if X - sum <= sorted_A[0]:
    print(0)
    exit()
print(X - sum)

