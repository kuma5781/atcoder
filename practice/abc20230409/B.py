s = input()  # 長さ8の文字列Sを受け取る

# 条件1のチェック
b_indexes = [i for i in range(len(s)) if s[i] == "B"]
if (b_indexes[0] + b_indexes[1]) % 2 == 0:
    print("No")
    exit()

# 条件2のチェック
r_indexes = [i for i in range(len(s)) if s[i] == "R"]

k_index = s.index("K")
if not (r_indexes[0] < k_index < r_indexes[1]):
    print("No")
    exit()