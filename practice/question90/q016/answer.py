# pypyでのみ正解になる
N = int(input())
A, B, C = map(int, input().split())
S = []

for i in range(10000):
    for j in range(10000):
        if N >= (A * i + B * j) and (N - (A * i + B * j)) % C == 0:
            k = (N - (A * i + B * j)) // C
            if i + j + k < 10000:
                S.append(i + j + k)

print(min(S))
