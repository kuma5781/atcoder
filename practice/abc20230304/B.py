N, Q = map(int, input().split())

yellow = set()
red = set()
for i in range(Q):
    e1, e2 = map(int, input().split())
    if e1 == 1:
        if e2 in yellow:
            red.add(e2)
        else:
            yellow.add(e2)
    elif e1 == 2:
        red.add(e2)
    else:
        if e2 in red:
            print("Yes")
        else:
            print("No")