N, K = map(int, input().split())

mod = 1000000007

# べき乗ごとにmodを取るときはpowを使う
if N == 1:
    print(K)
    exit()
elif N == 2:
    print((K * (K - 1)) % mod)
    exit()
else:
    ans = (K * (K - 1) * pow(K - 2, N - 2, mod)) % mod
print(ans)
