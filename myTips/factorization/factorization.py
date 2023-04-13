# 因数の数を求める
def fac(x):
    cnt = 0
    limit = int(x ** 0.5)
    # Xは素数でない限り、2からルートXまでに必ず約数を持つ
    for i in range(2, limit + 1):
        if x % i == 0:
            # 同じ数で連続で割り切れる場合があるので、whileで回す
            while x % i == 0:
                cnt += 1
                x //= i
    if x != 1:
        cnt += 1
    return cnt

# 因数分解する関数
# 返り値には、[[素因数, 指数], [素因数, 指数], ...]の形で因数分解結果が入る
def factorization(n):
    arr = []
    limit = int(n ** 0.5)
    tmp = n
    for i in range(2, limit + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])

    return arr
