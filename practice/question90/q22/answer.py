def gcd(A, B):
    while A > 0 and B > 0:
        if A >= B:
            A = A % B
        else:
            B = B % A
    if A > 0:
        return A
    else:
        return B

A, B, C = map(int, input().split())

# 立方体にするには。すべての辺の最大公約数を求める
G = gcd(A, B)
G = gcd(G, C)

# 各辺を最大公約数で割った商を求める（商が何回分割するかを表す）
# もともとの辺の長さと最大公約数が同じ場合1になるので、辺の数分1を引く
print(A // G + B // G + C // G - 3)
