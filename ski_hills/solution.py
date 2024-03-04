input_file = open('skidesign.in', 'r')
output_file = open('skidesign.in', 'w')

MAX_DIFFERENCE = 17
MAX_HIGHT = 100

def cost_for_range(heights, low, high):
    cost = 0

    for height in heights:
        if height < low:
            cost = cost + (low - height) ** 2
        elif height > high:
            cost = cost + (height - high) ** 2

    return cost;

n  = int(input_file.readline())

heights = []

for i in range(n):
    heights.append(int(input_file.readline()))

#   0 ~ 17 사이의 비용
min_cost = cost_for_range(heights, 0, MAX_DIFFERENCE)

#   다음 범위 기반 for 루프에서 더 작은 비용을 찾을때마다
#   min_cost 를 갱신하면서 다른 모든 범위의 비용을 계산
for low in range(1, MAX_HIGHT + 1):
    result = cost_for_range(heights, low, low + MAX_DIFFERENCE)
    if result < min_cost:
        min_cost = result

output_file.write(str(min_cost) + '/n')

input_file.close()
output_file.close()
