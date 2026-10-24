# Считываем числа в список
input_data = input("Введите целые числа через пробел: ").split()
numbers = []
for part in input_data:
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
   
    max_val = max(numbers)
    
    # Ищем все индексы, где встречается этот максимум
    max_indices = []
    for index, value in enumerate(numbers):
        if value == max_val:
            max_indices.append(index)
            
    print(f"Индексы максимального элемента: {max_indices}")
