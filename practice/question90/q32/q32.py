import itertools

# ある人や物の選び方の問題は順列を使う
# そしたら使ったものから選ばないという処理も必要ない
# 本問題ではng_listだけ考慮すればよい

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

ng_list = [set() for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    ng_list[x - 1].add(y - 1)
    ng_list[y - 1].add(x - 1)

ans = 100000

# 走者の順列を作成
# 順列の各要素（plan）で以下の操作をする
## 2番目以降の走者で前者がng_listに入っていないか確認する
### ng_listに入っている場合、ansの初期値を渡して、その選び方を排除する（ansの初期値をansとの比較対象にする）
### ng_listに入っていない場合、その走者のj区における時間をbufに足して、次の走者で同じ検証をする
### 順列の各要素の操作完了後、ansとその選ぶ方で算出した時間の小さい方をansに代入する

for plan in itertools.permutations(range(N)):
  buf = 0
  for i, n in enumerate(plan):
    if i != 0:
      if plan[i-1] in ng_list[n]:
        buf = 100000
        break
    buf += A[n][i]
  ans = min(ans, buf)

if ans == 100000:
  print(-1)
else:
  print(ans)
