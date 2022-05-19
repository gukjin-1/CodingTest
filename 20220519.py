import sys

N = int(sys.stdin.readline())
li = [0 for _ in range(N+1)]
li[1] = 1

for i in range(2, N+1):
    li[i] = li[i-1] + li[i-2]

print(li[-1])