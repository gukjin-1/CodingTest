n = int(input())


li = [int(input()) for _ in range(n)]
if n <= 1:
  print(0)


else:
  count = 0
  rev = li[1:n]
  dasom = li[0]
  rev = sorted(rev,reverse=True)

  while rev[0] >= dasom:
    dasom +=1
    rev[0] -=1
    count+=1
    rev = sorted(rev,reverse=True)



  print(count)