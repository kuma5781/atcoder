N = int(input())

for i in range(N, 920):
    n_str = str(i)
    if int(n_str[0]) * int(n_str[1]) == int(n_str[2]):
        print(i)
        break