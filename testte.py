from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.axis import DateAxis
from datetime import date
from copy import deepcopy

wb = Workbook()
ws = wb.active

# данные для построения диаграммы
rows = [
    ['Date', 'Batch 1', 'Batch 2', 'Batch 3'],
    [date(2015,9, 1), 40, 30, 25],
    [date(2015,9, 2), 40, 25, 30],
    [date(2015,9, 3), 50, 30, 45],
    [date(2015,9, 4), 30, 25, 40],
    [date(2015,9, 5), 25, 35, 30],
    [date(2015,9, 6), 20, 40, 35],
]
for row in rows:
    ws.append(row)

# ДИАГРАММА №1
# создаем объект диаграммы
chart1 = LineChart()
# заголовок диаграммы
chart1.title = "Линейная диаграмма"
# установим цветовую схему диаграммы
chart1.style = 13
# подпись оси `y`
chart1.y_axis.title = 'Размер'
# показывать данные на оси (для LibreOffice Calc)
chart1.y_axis.delete = False
# подпись оси `x`
chart1.x_axis.title = 'Номер теста'
chart1.x_axis.delete = False
# выберем 4 столбца с данными для оси `y` 
# в итоге получим 4 графика
data = Reference(ws, min_col=2, max_col=4, min_row=1, max_row=7)
# добавляем данные в объект диаграммы
chart1.add_data(data, titles_from_data=True)
# ТЕПЕРЬ ЗАДАДИМ СТИЛЬ ЛИНИЙ 
# ЛИНИЯ С ДАННЫМИ ИЗ 1 СТОЛБЦА ДАННЫХ
line1 = chart1.series[0]
# символ маркера для текущего значения
line1.marker.symbol = "x"
# цвет заливки маркера
line1.marker.graphicalProperties.solidFill = "FF0000"
line1.marker.graphicalProperties.line.solidFill = "FF0000"
# не заливаем линию между маркерами (прозрачная)
line1.graphicalProperties.line.noFill = True
# ЛИНИЯ С ДАННЫМИ ИЗ 2 СТОЛБЦА ДАННЫХ
line2 = chart1.series[1]
# цвет заливки линии графика
line2.graphicalProperties.line.solidFill = "00AAAA"
# делаем линию пунктирной
line2.graphicalProperties.line.dashStyle = "sysDot"
# ширина указывается в EMU
line2.graphicalProperties.line.width = 100050
# ЛИНИЯ С ДАННЫМИ ИЗ 3 СТОЛБЦА ДАННЫХ
line3 = chart1.series[2]
# символ маркера для текущего значения
line3.marker.symbol = "triangle"
# покрасим маркер в другой цвет
line1.marker.graphicalProperties.solidFill = "FF0000"
line3.marker.graphicalProperties.line.solidFill = "0000FF"
# делаем линию гладкой
line3.smooth = True
# добавим диаграмму на лист, в ячейку "A10"
ws.add_chart(chart1, "A10")

# ДИАГРАММА №2
# скопируем первую диаграмму
stacked = deepcopy(chart1)
# диаграмма с накоплением
stacked.grouping = "stacked"
stacked.title = "Графики с накоплением"
ws.add_chart(stacked, "A27")

# ДИАГРАММА №3
percent_stacked = deepcopy(chart1)
# диаграмма с процентным накоплением
percent_stacked.grouping = "percentStacked"
percent_stacked.title = "Графики с процентным накоплением"
ws.add_chart(percent_stacked, "A44")

# ДИАГРАММА №4 с датами по оси `x`, все линии
# графиков будут иметь стиль по умолчанию
# создаем объект диаграммы
chart2 = LineChart()
chart2.title = "Графики с осью дат"
# установим другую цветовую схему
chart2.style = 12
# подпись оси `y`
chart2.y_axis.title = "Размер"
chart2.y_axis.delete = False
# поперечная ось
chart2.y_axis.crossAx = 500
# подпись оси `x`
chart2.x_axis.title = "Дата"
chart2.x_axis.delete = False
chart2.x_axis = DateAxis(crossAx=100)
# формат отображения дат на оси `x`
chart2.x_axis.number_format = 'd-mmm'
# задаем временную единицу даты
chart2.x_axis.majorTimeUnit = "days"
# добавляем выборку данных из первой диаграммы
chart2.add_data(data, titles_from_data=True)
# делаем выборку данных для оси `x`
dates = Reference(ws, min_col=1, min_row=2, max_row=7)
chart2.set_categories(dates)
ws.add_chart(chart2, "A61")

# сохраняем и смотрим что получилось
wb.save("line.xlsx")