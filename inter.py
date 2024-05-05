import pandas as pd
import numpy as np

# Загрузка данных из файла Excel
df = pd.read_excel('Выгрузка для ЛАБ5-6.xlsx')

# Замена None на NaN
df.replace('None', np.nan, inplace=True)

# Определение числовых столбцов
numeric_columns = df.select_dtypes(include=[np.number]).columns

# Преобразование числовых значений в числовой формат и интерполяция
df[numeric_columns] = df[numeric_columns].interpolate(method='polynomial', order=2, limit_direction='both', limit_area='inside')

# Сохранение измененного DataFrame в файл Excel
df.to_excel('Выгрузка_с_заполненными_none.xlsx', index=False)
