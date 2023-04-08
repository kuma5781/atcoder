from collections import deque

Q = int(input())
s = deque()
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        s.appendleft(x)
    elif t == 2:
        s.append(x)
    else:
        print(s[x-1])
