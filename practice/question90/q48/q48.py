N, K = map(int, input().split())
li = []
# A-Bを求め、満点になるケースも1分間で考える
for i in range(N):
    A, B = map(int, input().split())
    li.append(B)
    li.append(A-B)
li.sort(reverse=True)
print(sum(li[:K]))
