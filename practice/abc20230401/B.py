S = [None] * 8
for i in range(8):
    S[i] = input()

column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = ['8', '7', '6', '5', '4', '3', '2', '1']

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(column[j] + row[i])