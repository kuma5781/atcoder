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
        print("rootu = " + str(rootu))
        print("rootv = " + str(rootv))
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    def same(self, u, v):
        return self.root(u) == self.root(v)


N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(Q)]

uf = unionfind(N)
for tp, u, v in queries:
    if tp == 1:
        uf.unite(u, v)
    else:
        if uf.same(u, v):
            print("Yes")
        else:
            print("No")