# python行列の回転

## 行列の90度右回転

```python
# inputは回転前の二次元配列
def rotate(A):
    return [[A[j][N - 1 - i] for j in range(N)] for i in range(N)]
```

### 別解

以下の手順でも行列を90度右回転することができる

- 行列の上下を入れ替える
    - A[::-1]で上下を入れ替えれる
- 行列を転置する
    - zip(*A)で転置する
    - mapで各要素をlist化しているのは、zipの結果がタプルになるため

```python
def another_rotate(A):
    return list(map(list, zip(*A[::-1])))
```

## 行列の90度左回転

```python
def rotate(A):
    # 行列を反転する関数
    return [[A[N - 1 - j][i] for j in range(N)] for i in range(N)]
```

### 別解

行列の90度右回転の理論を利用して以下の手順で90度左回転する

- 行列を転置する
- 行列の上下を入れ替える

```python
def another_rotate(A):
    return list(map(list, zip(*A)))[::-1]
```

参考にした記事

[https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c](https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c)