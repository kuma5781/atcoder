class unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1) # 全要素を親がない-1で初期化する
        self.size = [1] * (n + 1) # 全要素連結していないサイズ1で初期化する

    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    def same(self, u, v):
        return self.root(u) == self.root(v)

H, W = map(int, input().split())
S = [None] * H
for i in range(H):
    S[i] = input()

# この問題は各グリッドに数値を割り振る必要がある。1, 2, 3行目と増えるごとにWずつ増えるとする。
# このとき、各グリッドの数値はi * W + jで表される。
N = H * W
uf = unionfind(N)
for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            continue
        # ここから"#"限定の処理
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni = i + di
                nj = j + dj
                # H, Wにグリッド外であればスキップ
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                # 周りのマスで"#"でない場合はスキップ
                if S[ni][nj] != "#":
                    continue
                # 自分自身のマスはスキップ
                if ni == i and nj == j:
                    continue
                uf.unite(i * W + j, ni * W + nj)

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            continue
        v = i * W + j
        if uf.root(v) == v:
            ans += 1

print(ans)
