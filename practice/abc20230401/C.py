from bisect import bisect_left

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# a_i - a_j = x となる (i,j) が存在するかどうかを調べる
if n == 1:  # 要素が1つの場合
    print("No")
    exit()

if x == 0:  # xが0の場合
    print("Yes")
    exit()

for i in range(n):
    idx = bisect_left(a, a[i]+x)  # a_i + x が挿入されるべきインデックス
    if idx < n and a[idx] == a[i]+x:
        print("Yes")
        exit()

# setでもできる
# A = set(a)
# for i in range(n):
#     if a[i] + x in A:
#         print("Yes")
#         exit()

print("No")