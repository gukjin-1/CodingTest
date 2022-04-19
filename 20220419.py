n = int(input())

li = []

for i in range(n):
  a = int(input())
  li.append(a)

li.sort(reverse=True)

tip = 0

for i in range(1,len(li)+1):
  b = li[i-1] - (i-1)
  if b>0:
    tip += b
print(tip)