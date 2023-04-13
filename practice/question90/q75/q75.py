# 因数の数を求める
def fac(x):
    cnt = 0
    limit = int(x ** 0.5)
    for i in range(2, limit + 1):
        if x % i == 0:
            while x % i == 0:
                cnt += 1
                x //= i
    if x != 1:
        cnt += 1
    return cnt

N = int(input())
ans = 0
tmp = 1
cnt = fac(N)
while tmp < cnt:
    tmp *= 2
    ans += 1
print(ans)