n, money = map(int,input().split())

li = []

for i in range(n):
  li.append(int(input()))


li.sort(reverse = True)

a = 0

for i in li:
  if i > money:
    pass
  else:
    a += money // i 
    money %= i
    if money == 0:
      break
print(a) 