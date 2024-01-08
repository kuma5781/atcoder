N = int(input())
D = list(map(int, input().split()))

ans = 0
for i in range(1, N + 1):
    for j in range(1, D[i - 1] + 1):
        s = set()
        for k in range(len(str(i))):
            s.add(int(str(i)[k]))
        for k in range(len(str(j))):
            s.add(int(str(j)[k]))
        if len(s) == 1:
            ans += 1

print(ans)