N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None] * N
dp[0] = 0
dp[1] = A[0]

for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

Ans = []
Place = N
while True:
    Ans.append(Place)
    if Place == 1:
        break

    # dp, Aは0始まり、Placeは1始まりなのでそれぞれ合わせる
    # dpは各部屋、Aは各辺を意味するのでAの総数はdpより1小さくなる
    if dp[Place - 1] == dp[Place - 2] + A[Place - 2]:
        Place -= 1
    else:
        Place -= 2

Ans.reverse()
print(len(Ans))
print(*Ans)
