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

A, B = map(int, input().split())
print(gcd(A, B))
