N = int(input())
S = list(input())

flg = True
for i in range(len(S)):
    if S[i] == ',' and flg:
        S[i] = "."
    if S[i] == '"':
        flg = not flg

print("".join(S))