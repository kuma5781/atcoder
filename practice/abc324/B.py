N = int(input())

while True:
    if N % 2 == 0:
        N = N // 2
    elif N % 3 == 0:
        N = N // 3
    elif N == 1:
        print("Yes")
        break
    else:
        print("No")
        break