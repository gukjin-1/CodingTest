n = int(input())

li = []

for i in range(n):
  a = list(map(int,input().split()))
  li.append(a)
print(li)

# li.sort(key = lambda x:x[0])
li.sort(key = lambda x:x[1])

cnt = 1
end = li[0][1]
for i in range(1,n):
  if li[i][0] >= end :
    cnt+=1
    end = li[i][1]
