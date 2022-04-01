n = input()

a0 = 0
a1 = 0

if n[0] == '0':
  a1 +=1
else:
  a0 +=1


for i in range(len(n)-1):
  if n[i] != n[i+1]:
    if n[i+1] == '1':
      a0+=1
    else:
      a1+=1
print(min(a0,a1))