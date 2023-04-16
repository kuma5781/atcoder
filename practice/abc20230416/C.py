# N = int(input())
# Q = int(input())
# query = [list(map(int, input().split())) for _ in range(Q)]
# box = [[] for _ in range(N)]

# for k in range(Q):
#     if query[k][0] == 1:
#         i = query[k][1]
#         j = query[k][2]
#         box[j - 1].append(i)
#     elif query[k][0] == 2:
#         i = query[k][1]
#         box[i - 1].sort()
#         print(" ".join(map(str, box[i - 1])))
#     else:
#         i = query[k][1]
#         tmp = []
#         for j in range(len(box)):
#             if i in set(box[j]):
#                 tmp.append(j + 1)
#         tmp.sort()
#         print(" ".join(map(str, tmp)))

N = int(input())
Q = int(input())
# 箱i番目に入っているカードのリスト（カードの重複あり）
box_list = [[] for _ in range(N)]
# カードi番目が入っている箱の集合（箱の重複はなし）
card_list = [set() for _ in range(2 * 10 ** 5 + 1)]

for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        i = cmd[1]
        j = cmd[2]
        box_list[j - 1].append(i)
        card_list[i - 1].add(j)
    elif cmd[0] == 2:
        print(*sorted(box_list[cmd[1] - 1]))
    else :
        print(*sorted(card_list[cmd[1] - 1]))
