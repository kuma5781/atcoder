N = int(input())
S = input()
cnt1 = 0
cnt2 = 0
for s in S:
    if s == "o":
        cnt1 += 1
    if s == "x":
        cnt2 += 1

if cnt1 > 0 and cnt2 == 0:
    print("Yes")
else:
    print("No")