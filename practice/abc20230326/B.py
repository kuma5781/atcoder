R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]
F = []
T = [".", "#"]

for i in range(R):
    for j in range(C):
        if not B[i][j] in T:
            # bom威力、x座標、y座標
            F.append((int(B[i][j]), i, j))

for f in F:
    for i in range(R):
        for j in range(C):
            M = abs(f[2] - j) + abs(f[1] - i)
            if M <= f[0]:
                B[i][j] = "."

for i in range(R):
    ans = "".join(B[i])
    print(ans)