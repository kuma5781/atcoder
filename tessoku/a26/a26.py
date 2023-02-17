def isPrime(x):
    limit = int(x ** 0.5)
    for i in range(2, limit + 1):
        if x % i == 0:
            return False
    return True

Q = int(input())
X = [None] * Q
for i in range(Q):
    X[i] = int(input())

for i in range(Q):
    if isPrime(X[i]):
        print("Yes")
    else:
        print("No")
