n,m = map(int,input().split())

brand_m= []
brand_n = []

minpack = 1001
minsingle = 1001
for i in range(m):
  p,s = map(int,input().split())
  minpack = min (minpack,p)
  minsingle = min(minsingle,s)

result = 0

if minpack > minsingle*6 :
  result += n*minsingle
else:
  result += (n//6) * minpack

  if (n%6)*minsingle > minpack:
    result += minpack
  else:
    result +=(n%6)*minsingle

print(result)
