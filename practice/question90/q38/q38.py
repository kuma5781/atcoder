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
# 切り捨てずint型にしてもOKと思ったが、NG。切り捨てを使う方が吉。
ans = A * B // gcd(A, B)
if ans > 10 ** 18:
    print("Large")
else:
    print(ans)