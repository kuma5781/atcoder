from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

# RUN LENGTH DECODING list(tuple()) -> str
# example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L):
    res = ""
    for c, n in L:
        res += c * int(n)
    return res

# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1"
def runLengthEncodeToString(S):
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res


S=input()
T=input()

rleS = runLengthEncode(S)
rleT = runLengthEncode(T)

if len(rleS) < len(rleT):
    print("No")
    exit()

# ランレングス圧縮した結果で、以下のどちらかをすべて満たせればOK
# T, Sの連続する文字の長さがどちらも1
# T, Sの連続する文字の長さが2以上のとき、T >= SであればOK
for i in range(len(rleS)):
    # 前提として文字が同じであること
    if rleS[i][0] != rleT[i][0]:
        print("No")
        exit()
    #　条件1
    if rleS[i][1] == rleT[i][1] == 1:
        continue
    # 条件2
    elif rleS[i][1] == 1 and rleT[i][1] > 1:
        print("No")
        exit()
    elif rleS[i][1] <= rleT[i][1]:
        continue
    else:
        print("No")
        exit()

print("Yes")