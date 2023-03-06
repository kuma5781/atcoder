class unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n # 全要素を親がない-1で初期化する
        self.size = [1] * n # 全要素連結していないサイズ1で初期化する

    # 根を求める
    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 2頂点の根を結合する
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

    # 2頂点が同じグループに存在するか確認
    def same(self, u, v):
        return self.root(u) == self.root(v)

    # xを含む根付き木のサイズを求める
    def xsize(self, x):
        return self.size(self.root(x))


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
uLis = []
uf = unionfind(N)
for i in range(M):
    # unionfindでは0始まりの配列として扱うので、-1する
    uf.unite(edges[i][0] - 1, edges[i][1] - 1)
    uLis.append(edges[i][0] - 1)

# uが所属する連結成分を求める（根を求めてその根に+１する）
# u, vどちらか一方で良い。どちらも同じ連結成分であることは自明。
eNum = [0] * N
for i in range(M):
    eNum[uf.root(uLis[i])] += 1

# ここ理解できてない
# なぜNより小さいの数の根を求めるといける？
# 各頂点のrootを求める?
nNum = [0] * N
for i in range(N):
    nNum[uf.root(i)] += 1

print(eNum)
print(nNum)

if eNum == nNum:
    print('Yes')
else:
    print('No')
