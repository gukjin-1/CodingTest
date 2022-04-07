n = int(input())
li = list(map(int,input().split()))
li.sort(reverse=True)
for i in range(n):
  li[i] += i+1
print(max(li)+1)