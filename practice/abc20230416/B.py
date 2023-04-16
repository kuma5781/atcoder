N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def another_rotate(A):
    return list(map(list, zip(*A[::-1])))

def rotate(A):
    # 行列を反転する関数
    return [[A[N - 1 - j][i] for j in range(N)] for i in range(N)]

def get_positions(matrix):
    # 行列の 1 の要素の位置をリストで返す関数
    positions = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                positions.append((i, j))
    return positions

positions_b = get_positions(B)

for _ in range(4):
    # A を 4 回回転する
    A = another_rotate(A)
    positions_a = get_positions(A)
    # AがBの部分集烏合かどうか判定
    if set(positions_a) <= set(positions_b):
        print("Yes")
        exit()

print("No")