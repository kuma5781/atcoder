H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
else:
    # 2*2のマスの中で一個しかLEDを光らせることができないため縦、横をそれぞれ2で割った商を求める
    # 縦、横それぞれ奇数個のときにLEDを一つ多く増やせるため+1してる（ただ偶数個のとき+1して2で割った商を求めても結果+1しなかったときと変わらないから共通で1足している）
    h2 = (H + 1) // 2
    w2 = (W + 1) // 2
    print(h2 * w2)