n, l = map(int,input().split())

m = list(map(int,input().split()))

m.sort()

start = m[0]
end = m[0] + l
cnt = 0

for i in range(n):
  if start <=m[i] < end:
    continue
  else:
    start = m[i]
    end = m[i] + l
    cnt +=1
print(cnt+1)