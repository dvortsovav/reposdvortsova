
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_index = numbers.index(None)  # Предполагаем, что пропущенный элемент обозначен как None
# Вычислим сумму и количество элементов, исключая пропущенный
total_sum = sum(num for num in numbers if num is not None)
count = len(numbers)  # Общее количество элементов, включая пропуск
# Рассчитаем среднее арифметическое
average = total_sum / count  # Исключаем пропуск из суммы
# Заменяем пропущенный элемент средним арифметическим
numbers[missing_index] = average
print("Измененный список:", numbers)
