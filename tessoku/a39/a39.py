N = int(input())
A = []

for i in range(N):
    L, R = map(int, input().split())
    # 二次元配列は先頭要素に対してソートするので、終了時間であるRを先頭に持ってくる
    A.append([R, L])

A.sort()

cnt = 0
currentTime = 0
for i in range(N):
    if A[i][1] >= currentTime:
        currentTime = A[i][0]
        cnt += 1

print(cnt)

