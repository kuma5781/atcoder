S = list(input())

for i in range(int(len(S) / 2)):
    t1 = S[2 * i]
    t2 = S[2 * i + 1]
    S[2 * i] = t2
    S[2 * i + 1] = t1

print("".join(S))