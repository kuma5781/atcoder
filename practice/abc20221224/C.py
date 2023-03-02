S = input()
count = 0
flg = False
for i in range(len(S)):
    if flg == False:
        flg = True
        continue
    if S[i: i + 2] == "00":
        count += 1
        flg = False

print(len(S) - count)

# 別解
# S = input()
# cntNum00 = S.count("00")
# allCnt = len(S)
# if cntNum00 != 0:
#     print(allCnt - cntNum00)
# else:
#     print(allCnt)