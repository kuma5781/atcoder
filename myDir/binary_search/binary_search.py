# algorithm
def binary_search(list, value):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# library
## 挿入できる場所を求める

import bisect
# sort済みの配列
li = [2, 5, 8, 13, 13, 18, 25, 30]

# 挿入できるリストの添字を返す。同じ値がある場合に最も左側の添字を返す
ind = bisect.bisect_left(li, 10)
print(ind)
# 挿入できるリストの添字を返す。同じ値がある場合に最も右側の添字を返す
# bisect = bisect_right
ind = bisect.bisect_right(li, 10)
print(ind)
ind = bisect.bisect(li, 10)
print(ind)
