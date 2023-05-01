L, R = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
# 最小の桁数と最大の桁数を求める
min_digit = len(str(L))
max_digit = len(str(R))

for i in range(min_digit, max_digit + 1):
    min_num = max(L, 10 ** (i - 1))
    max_num = min(R, 10 ** i - 1)
    ans += (max_num - min_num + 1) * (min_num + max_num) // 2 * i

print(ans % mod)