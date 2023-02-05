N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(N)]

for a, b in edges:
    G[a - 1].append(b)
    G[b - 1].append(a)

for i in range(N):
    output = ""
    output += str(i + 1)
    output += ": {"
    output += ", ".join(map(str, G[i]))
    output += "}"
    print(output)