# ダメな例
N, M = map(int, input().split())
A = list(map(int, input().split()))

hanabi_day_set = set()
for i in range(M):
    hanabi_day_set.add(A[i])

day_flg_list = [False] * (N + 1)
for i in range(1, N + 1):
    if i in hanabi_day_set:
        day_flg_list[i] = True

for i in range(1, N + 1):
    count = 0
    # この方法だと一つの出力までO(N)かかる
    for j in range(i, N + 1):
        if day_flg_list[j]:
            print(count)
            break
        else:
            count += 1


# 方法1
N, M = map(int, input().split())
A = list(map(int, input().split()))

# この方法が思いつかなかった
# 一日ずつ確認していくが、それが次の花火とどれくらい離れているかを考える
# 一番シンプルかもしれない
day = 1
for i in range(M):
    # この方法だと一つの出力までO(1)でいける
    while A[i] - day >= 0:
        print(A[i] - day)
        day += 1

# 方法2
N, M = map(int, input().split())
A = list(map(int, input().split()))

hanabi_day_set = set()
for i in range(M):
    hanabi_day_set.add(A[i])

day_flg_list = [False] * (N + 1)
for i in range(1, N + 1):
    if i in hanabi_day_set:
        day_flg_list[i] = True

# この方法は後ろから考えていくことでその前の要素がどれだけ離れているかを考える
# 最初の要素（元のリストでは一番後ろ）から花火が上がらない場合、+1していく
ans_list = [0]
for i in range(N - 1, 0, -1):
    if day_flg_list[i]:
        ans_list.append(0)
    else:
        ans_list.append(ans_list[N - i - 1] + 1)

rev_list = list(reversed(ans_list))

for i in range(N):
    print(rev_list[i])