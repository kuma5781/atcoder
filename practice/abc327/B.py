n = int(input())
i = 1
ans = -1

while i ** i <= n:
  if i ** i == n:
    ans = i
    break
  i += 1

print(ans)