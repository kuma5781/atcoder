N = int(input())
S = [None] * N
for i in range(N):
    S[i] = input()
cnt = 0
for i in range(N):
    if S[i] == "For":
        cnt += 1
if cnt > N / 2:
    print("Yes")
else:
    print("No")