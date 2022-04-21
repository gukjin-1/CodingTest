n = int(input())
dis = list(map(int,input().split()))
oil = list(map(int,input().split()))

m = oil[0]
money = 0
for i in range(n-1):
  if m>oil[i]:
    m = oil[i]
  money += (m * dis[i])
