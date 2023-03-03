S = input()
box = set()
memo = [set()]
index = 0
flg = True

for s in S:
    if s == "(":
        index += 1
        memo.append(set())
    elif s == ")":
        box -= memo[index]
        memo[index] = set()
        index -= 1
    elif s in box:
        flg = False
        break
    else:
        box.add(s)
        memo[index].add(s)

if flg:
    print("Yes")
else:
    print("No")