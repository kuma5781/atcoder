N = int(input())
S = input()
T = set([(0, 0)])
X = 0
Y = 0

for i in range(N):
    if S[i] == "R":
        X += 1
    elif S[i] == "L":
        X -= 1
    elif S[i] == "U":
        Y += 1
    elif S[i] == "D":
        Y -= 1

    if (X, Y) in T:
        print("Yes")
        break
    T.add((X, Y))
else:
    print("No")