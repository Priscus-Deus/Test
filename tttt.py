from datetime import datetime

def format_date(date_str):
    # Преобразование строки в объект datetime
    date_object = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    # Определение дня недели на русском языке
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    # Форматирование даты
    formatted_date = date_object.strftime(f'{days[date_object.weekday()]} %m.%d.%Yг.')
    return formatted_date

# Пример использования функции
input_date = '2024-07-02 00:00:00'
result = format_date(input_date)
print(result)
