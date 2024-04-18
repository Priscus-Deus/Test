def find_median_height(heights):
    sorted_heights = sorted(heights)
    n = len(sorted_heights)

    if n % 2 == 0:
        # Если четное количество элементов, берем среднее между двумя средними значениями
        median = (sorted_heights[n // 2 - 1] + sorted_heights[n // 2]) / 2
    else:
        # Если нечетное количество элементов, берем средний элемент
        median = sorted_heights[n // 2]

    return median

# Ввод данных
n = int(input())
heights = list(map(int, input().split()))

# Нахождение медианы
median_height = find_median_height(heights)
print(median_height)
