# 配列の要素を選択できる全パターンを調べる
def bitFullSearch(list):
    for i in range(1 << len(list)):
        combination = []
        for j in range(len(list)):
            if ((i >> j) & 1):
                combination.append(list[j])
        print(combination)