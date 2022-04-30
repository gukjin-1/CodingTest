t = int(input())

for _ in range(t):
    n = int(input())
    heights = [int(x) for x in input().split()]
    heights.sort()

    max_level = 0
    for i in range(2, n):
        max_level = max(max_level, abs(heights[i] - heights[i - 2]))

    print(max_level)