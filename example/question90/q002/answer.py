from itertools import product

N = int(input())
product_list = list(product('()', repeat=N))

# やること
# Nが奇数かどうか
# 奇数であればprint()
# 偶数の場合、以下
# 直積で表した要素で"("の数がN // 2 に等しければ後続の処理
# 直積で表した要素の中の文字をif文で条件分岐
# "("と")"の数を最終的に足して0になればOK
# それ以外であればbreak

for tuple in product_list:
    cnt = 0
    if tuple.count("(") == N / 2:
        for t in tuple:
            if t == "(":
                cnt += 1
                if cnt > N / 2:
                    break
            elif t == ")":
                cnt -= 1
                if cnt < 0:
                    break
        if cnt == 0:
            res = "".join(tuple)
            print(res)
