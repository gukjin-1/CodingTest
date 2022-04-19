n = int(input())

li = [int(input()) for i in range(n)]

count = 0

for i in range(n-1,0,-1):
  if li[i] <= li[i-1]:
    count += (li[i-1]-li[i]+1)
    li[i-1] = li[i] -1
print(count)