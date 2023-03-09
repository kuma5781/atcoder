import math
a, b, d = map(int, input().split())

# 角度法を弧度法（ラジアン）に変換
d_rad = math.radians(d)

# 二次元回転行列の公式に当てはめる
a_rotated = a * math.cos(d_rad) - b * math.sin(d_rad)
b_rotated = a * math.sin(d_rad) + b * math.cos(d_rad)

print(a_rotated, b_rotated)
