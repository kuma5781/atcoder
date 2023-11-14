
def rotate(A, N):
    return [[A[j][N - 1 - i] for j in range(N)] for i in range(N)]

A = [[None] * 9] * 9
for i in range(9):
    A[i] = list(map(int, input().split()))

row = False
col = False
box = False

for i in range(9):
    if len(A[i]) != len(set(A[i])):
        break
else:
    row = True

rotate_A = rotate(A, 9)
for i in range(9):
    if len(rotate_A[i]) != len(set(rotate_A[i])):
        break
else:
    col = True

boxA_ok_sum = 0
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        box_A = []
        for k in range(3):
            for l in range(3):
                box_A.append(A[i + k][j + l])
        if len(box_A) == len(set(box_A)):
            boxA_ok_sum += 1

if boxA_ok_sum == 9:
    box = True


if row and col and box:
    print("Yes")
else:
    print("No")