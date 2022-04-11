N, K = map(int,input().split())

sum_mini = K*(K+1) // 2

if sum_mini > N:
  print(-1)
elif (N-sum_mini) % K == 0:
  print(K-1)
else:
  print(K)

