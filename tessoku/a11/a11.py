N, X = map(int, input().split())
A = list(map(int, input().split()))

"""
二分探索

Parameters
----------
X : int
    探したい値
list : list
    探索対象の配列
"""
def list_binary_search(x, list):
    N = len(list)
    # 二分探索では必ずソートされていることが前提
    sorted_list = sorted(list)
    L = 0
    R = N - 1
    # L=Rになったら最後の探索対象になるので、L<=Rとする
    while L <= R:
        M = (L + R) // 2
        if x < sorted_list[M]:
            R = M - 1
        if x == sorted_list[M]:
            return M
        if x > sorted_list[M]:
            L = M + 1
    return -1

ans = list_binary_search(X, A)
print(ans + 1)
