def Power(a, b, m):
    ans = 1
    # 1<=b<=10^9のため、bの値が2^30を超えることはない
    for i in range(30):
        wari = 2 ** i
        if (b // wari) % 2 == 1:
            ans = (ans * a) % m
        a = (a * a) % m
    return ans

# a÷b を m で割った余りを返す関数
def Division(a, b, m):
	return (a * Power(b, m - 2, m)) % m

n, r = map(int, input().split())
M = 1000000007

a = 1
for i in range(1, n + 1):
    a = (a * i) % M

b = 1
for i in range(1, r + 1):
    b = (b * i) % M
for i in range(1, n - r + 1):
    b = (b * i) % M

# a / b
# = a * b ^ (m - 2)

print(Division(a, b, M))