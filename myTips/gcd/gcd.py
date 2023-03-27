# ユークリッド互除法を使って最大公約数を求める
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