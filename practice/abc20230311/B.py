N = int(input())
A = list(map(int, input().split()))
call = set()

for i in range(N):
    if not i + 1 in call:
        call.add(A[i])

ans = []
for i in range(1, N + 1):
    if not i in call:
        ans.append(str(i))

print(len(ans))
print(" ".join(ans))