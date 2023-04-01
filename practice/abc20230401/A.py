N = int(input())
S = input()

for i in range(len(S)):
    if i == len(S) - 1:
        print("Yes")
        break
    if S[i] == "M" and S[i + 1] == "F":
        continue
    elif S[i] == "F" and S[i + 1] == "M":
        continue
    else:
        print("No")
        break