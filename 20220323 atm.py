## ATM

num = int(input())
s = list(map(int,input().split()))

s.sort()
for i in range(num):
  for j in range(i+1):
    num +=s[j]
print(num)


