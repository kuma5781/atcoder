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

"""
繰り返し二乗法

Parameters
----------
x : int
    底
n : int
    指数
m : int
    剰余
"""
def myPow(x, n, m):
    ans = 1
    # すべての桁を1かどうか確認して、1であれば答えにxをかける
    while n > 0:
        # 最小桁が1のときだけ、ansにxをかける
        if n % 2 == 1:
            ans = ans * x % m
        # 次の桁数が1の場合xの2乗を答えに掛ける必要があるので、ここでxを2乗しておく
        x = x * x % m
        # 次の桁へ
        n >>= 1
    return ans

N = 1000000007
a, b = map(int, input().split())
print(myPow(a, b, N))

# pythonのpow関数を使う
N = 1000000007
a, b = map(int, input().split())
print(pow(a, b, N))

