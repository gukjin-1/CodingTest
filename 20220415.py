n, m = map(int, input().split())
li = sorted([int(input()) for _ in range(m)])
max_p = max_b = 0
for i in range(m):
    t = li[i] * ((m-i) if m-i <= N else n)
    if max_b < t:
        max_b = t
        max_p = li[i]
print(max_p, max_b)