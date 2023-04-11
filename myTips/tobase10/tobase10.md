##　10進数からN進数に変換する関数
```
// value：変換対象の値, base: 変換する進数
// 下記の関数は各要素にint型の数字を持つlistを返すのでその後の操作に注意が必要
// 実装例：q67.pyを参照
def base10int(value, base):
    if value >= base:
        yield from base10int(value // base, base)
    yield value % base

```

## N進数から10進数に変換する関数

```
// value：変換対象の値, base: 変換元の進数
// 既存のint関数で実現できる
int(value, base)
```

## N進数からM進数に変換する方法
- N進数を10進数に変換する
- 10進数をM進数に変換する

上記のようにN進数からM進数に直接変換するのは難しい