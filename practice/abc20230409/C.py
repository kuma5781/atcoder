H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 文字列の一部の文字を更新するときは以下の2通り方法がある
## 文字列をリストに変換して、リストの要素を更新する
## スライスを使って、文字列の一部を切り出して、切り出した部分に新しい文字列を代入する
for i in range(H):
    for j in range(W - 1):
        if S[i][j] == S[i][j+1] == "T":
            S[i] = S[i][:j] + "P" + "C" + S[i][j+2:]

for i in range(H):
    print(S[i])