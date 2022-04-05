li = []
while True:
  l,p,v = map(int,input().split())
  li.append([l,p,v])
  if l==0 | p == 0 | v ==0 :
    break

for i in range(len(li)-1):
  cnt = 0
  m = li[i][2]//li[i][1]
  cnt += m*li[i][0]
  if li[i][0] < li[i][2]%li[i][1] :
    cnt += li[i][0]
  else:
    cnt += li[i][2]%li[i][1]
  
  print(f'Case {i+1}: {cnt}')