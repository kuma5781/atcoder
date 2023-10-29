N, K = map(int, input().split())
A = list(map(int, input().split()))

"""
答えで二分探索

Parameters
----------
N : int
    Aの要素数
ans : int
    探したい値
A : list
    探索対象の配列
"""
def answer_binary_search(N, ans, A):
    # チラシが印刷されるまでの時間の最小値が1、最大値が10^9なので、それぞれL, Rに設定する
    L = 1
    R = 10 ** 9
    # 厳密にはL=Rになったとき、探索終了する
    while L < R:
        M = (L + R) // 2
        # M分で印刷した場合のチラシの枚数を計算する
        sum = 0
        for i in range(N):
            sum += M // A[i]
        # M分で印刷した場合のチラシの枚数が答えより小さい場合、M分で印刷した場合のチラシの枚数は答えになり得ないので、LをM+1にする
        if sum < ans:
            L = M + 1
        # M分で印刷した場合のチラシの枚数が答えより大きい場合、M分で印刷した場合のチラシの枚数は答えになり得るので、RをMにする(その後もう少し小さい値がないかwhileループで探索する)
        if sum >= ans:
            R = M
    return L

ans = answer_binary_search(N, K, A)
print(ans)