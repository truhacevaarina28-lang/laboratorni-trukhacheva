# Читаем строку, бьем по пробелам и превращаем в список целых чисел
input_data = input("Введите целые числа через пробел: ").split()
numbers = []
for part in input_data:
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    # Считаем все показатели 
    count_val = len(numbers)
    sum_val = sum(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = sum_val / count_val
    
    print(f"Количество: {count_val}")
    print(f"Сумма: {sum_val}")
    print(f"Минимум: {min_val}")
    print(f"Максимум: {max_val if 'max_value' in locals() else max_val}")
    print(f"Среднее: {avg_val:.2f}")