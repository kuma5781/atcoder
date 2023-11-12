N, T = input().split()
N = int(N)
S = [None] * N
for i in range(N):
    S[i] = input()

def ok(s):
    i, j, miss = 0, 0, 0
    # insert
    if (len(s) > len(T)):
        while j < len(T):
            if s[i] == T[j]:
                i += 1
                j += 1
            else:
                miss += 1
                if miss > 1:
                    return False
                i += 1
    # delete
    elif (len(s) < len(T)):
        while i < len(s):
            if s[i] == T[j]:
                i += 1
                j += 1
            else:
                miss += 1
                if miss > 1:
                    return False
                j += 1
    # replace
    else:
        while i < len(s):
            if s[i] == T[j]:
                i += 1
                j += 1
            else:
                miss += 1
                if miss > 1:
                    return False
                i += 1
                j += 1

    return True



ans = []
for i in range(N):
    if abs(len(T) - len(S[i])) > 1:
        continue
    if (ok(S[i])):
        ans.append(i + 1)

print(len(ans))
print(*ans)

