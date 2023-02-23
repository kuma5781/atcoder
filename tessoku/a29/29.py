def Power(a, b, m):
    ans = 1
    # 1<=b<=10^9のため、bの値が2^30を超えることはない
    for i in range(30):
        wari = 2 ** i
        if (b // wari) % 2 == 1:
            ans = (ans * a) % m
        a = (a * a) % m
    return ans

N = 1000000007
a, b = map(int, input().split())
print(Power(a, b, N))

