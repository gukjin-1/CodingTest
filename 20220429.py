import sys
t = int(input())

for i in range(t):
  cnt =1
  li = []

  n = int(input())
  for i in range(n):
    paper, interview = map(int,sys.stdin.readline().split())
    li.append([paper, interview])
  li.sort()
  max = li[0][1]

  for i in range(1,n):
    if max > li[i][1]:
      cnt +=1
      max = li [i][1]
  print(cnt)