N, K = map(int, input().split())

def base10int(value, base):
    if value >= base:
        yield from base10int(value // base, base)
    yield value % base

for i in range(K):
    decimal = int(str(N), 8)
    base9 = list(base10int(decimal, 9))
    for j in range(len(base9)):
        if base9[j] == 8:
            base9[j] = 5
    N = int("".join(list(map(str, base9))))

print(N)
