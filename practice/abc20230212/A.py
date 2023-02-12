# 文字列で受け取ったものを1文字ごとに分割して配列にする
s = [i for i in input()]

for i in range(len(s)):
    if s[i] == "0":
        s[i] = str(1)
    else:
        s[i] = str(0)

print("".join(s))