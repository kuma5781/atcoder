N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [None] * N
for i in range(N):
    S[i] = input()


# 方針
## 1.それぞれのプレイヤーの今の合計点を求める
## 2.その最大値を求めて、それぞれのプレイヤーの合計値と最大値の差を求める
### 2-1.最大値のものは問答無用で0でOK
### 2-2.それ以外のものは、最大値との差を求める。その際は選んでいない問題の点数を配列に入れて、ソートして、先頭から引いていく
### 2-3.最大値との差が0より小さくなったら、その時の引いた回数が答え
sum_score_list = [0] * N
for i in range(N):
    sum_score_list[i] += i + 1
    for j in range(M):
        if S[i][j] == 'o':
            sum_score_list[i] += A[j]

max_score = max(sum_score_list)

for i in range(N):
    if sum_score_list[i] == max_score:
        print(0)
        continue
    else:
        diff = max_score - sum_score_list[i]
        not_selected_list = []
        for j in range(M):
            if S[i][j] == 'x':
                not_selected_list.append(A[j])
        not_selected_list_sorted = sorted(not_selected_list, reverse=True)

        for j in range(len(not_selected_list_sorted)):
            diff -= not_selected_list_sorted[j]
            if diff < 0:
                print(j + 1)
                break