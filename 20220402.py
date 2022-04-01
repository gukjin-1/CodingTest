n,box = map(int,input().split())
if n == 0:
  print(0)

else:
  weight = list(map(int,input().split()))
  a= 0 
  count = 1
  for i in range(n-1,-1,-1):
    a += weight[i]
    if a > box:
      count+=1
      a = weight[i]
  print(count)