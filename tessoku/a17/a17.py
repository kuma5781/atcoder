N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None] * (N + 1)
dp[1] = 0
dp[2] = A[0]
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i - 2], dp[i - 2] + B[i - 3])

ans = []
# 各部屋を出力する必要があるためplaceを用意
place = N
while True:
    ans.append(place)
    if place == 1:
        break
    if dp[place] == dp[place - 1] + A[place - 2]:
        place -= 1
    else:
        place -= 2

print(len(ans))
print(*ans[::-1])

# dp = [None] * N
# dp[0] = 0
# dp[1] = A[0]

# for i in range(2, N):
#     dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

# Ans = []
# Place = N
# while True:
#     Ans.append(Place)
#     if Place == 1:
#         break

#     # dp, Aは0始まり、Placeは1始まりなのでそれぞれ合わせる
#     # dpは各部屋、Aは各辺を意味するのでAの総数はdpより1小さくなる
#     if dp[Place - 1] == dp[Place - 2] + A[Place - 2]:
#         Place -= 1
#     else:
#         Place -= 2

# Ans.reverse()
# print(len(Ans))
# print(*Ans)