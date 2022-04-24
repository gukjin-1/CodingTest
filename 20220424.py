a = input().split('-')

li = []
for i in a:
  cnt = 0
  s = i.split('+')
  for j in s:
    cnt += int(j)
  li.append(cnt)

n = li[0]
for i in range(1,len(li)):
  n -= li[i]
print(n)