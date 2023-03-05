N = int(input())
ans = 0
# X = AB, Y = CDとして X + Y = Nとなる個数を求める
# Xの値が決まるとき、Yの値も必然的に決まる
for i in range(1, N):
    X = i
    Y = N - i
    x = 0
    # jはXを構成する要素A, Bを表す
    j = 1
    # A*BがX以下となる数を精査していく
    # jの値がXの約数の場合count+1。もしjの二乗がXでない場合、2つの選び方が存在するのでcountをもう+1。
    while j * j <= X:
        if X % j == 0:
            x += 1
            if X != j * j:
                x += 1
        j += 1
    y = 0
    j = 1
    while j * j <= Y:
        if Y % j == 0:
            y += 1
            if Y != j * j:
                y += 1
        j += 1
    # x, yで求めた個数の積が選び方を考慮した個数になる
    ans += x * y

print(ans)
