a,b,c,m = map(int,input().split())

amount = 0

pirodo = 0

if a> m :
  print(0)
else:

  for _ in range(24):
    if pirodo + a <= m:
      pirodo += a
      amount += b
    elif pirodo -c >= 0 :
      pirodo -=c
  print(amount)