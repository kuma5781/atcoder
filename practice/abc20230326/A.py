N = int(input())
S = ["and", "not", "that", "the", "you"]
W = list(input().split())

for i in range(N):
    if W[i] in S:
        print("Yes")
        break
else:
    print("No")