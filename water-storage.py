n, d, t = map(int, input().split())

heights = list(map(int, input().split()))


front_index = -1
for i in range(1, n):
    if heights[i] < heights[i - 1]:
        front_index = i-1
        break

back_index = -1
for i in range(n - 2, -1, -1):
    if heights[i] < heights[i + 1]:
        back_index = i + 1
        break


water_height = min(heights[back_index], heights[front_index]) * (back_index - (front_index+1))

volume =  d * t * (water_height - sum(heights[front_index+1:back_index]))
print(volume)
