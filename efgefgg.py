import numpy as np

# Значения данных (замените их на ваши фактические данные)
data = [1.080, 1.685, None, 1.815, 1.770, 1.792, 1.616, 1.584, 1.603, None, 1.637, 1.669, 1.685, 1.786, 1.863, 1.861, None, 1.884, 1.993, 2.040, 2.102]

# Преобразуем список в массив numpy
data_array = np.array(data)

# Создадим копию массива, в которой пропущенные значения будут заменены на NaN
data_array_with_nan = np.where(data_array != None, data_array, np.nan)

# Вычислим разницу между соседними значениями
differences = np.diff(data_array_with_nan, n=2)

# Вычислим среднее значение разницы второго порядка, игнорируя NaN
mean_second_order_diff = np.nanmean(differences)

# Заполним пропущенные значения
for i in range(len(data)):
    if data[i] is None and i >= 2:  # Пропуски в первых двух значениях не могут быть заполнены
        data[i] = data[i - 1] + mean_second_order_diff

print(data)
