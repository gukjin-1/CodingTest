t = int(input())

for _ in range(t):
  a = int(input())
  b = list(map(int,input().split()))
  cnt = 0
  max = 0
  for i in range(a-1,-1,-1):
    if b[i] > max:
      max = b[i]
    else:
      cnt += max-b[i]

  print(cnt)