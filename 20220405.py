n,s,r = map(int,input().split())
damaged = list(map(int,input().split()))
extra = list(map(int,input().split()))

count = s

for i in extra:
  if i in damaged:
    damaged.remove(i)
    extra.remove(i)
    count -= 1

for i in damaged:
  for j in extra:
    if j-1 <= i <= j+1:
      extra.remove(j)
      count-=1
      break
    elif j+1 < i:
      break
print(count)