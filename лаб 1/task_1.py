numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0  # Заменяем пустое значение 0

sum_namber = sum(numbers)  # Сумма списка
quantity_namber = len(numbers)  # Кол-во чисел
average_namber = sum_namber / quantity_namber  # Средное арифметическое чисел

numbers[4] = average_namber  # Заменяем значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
