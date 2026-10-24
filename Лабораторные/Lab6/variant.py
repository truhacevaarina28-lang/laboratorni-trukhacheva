# Вводим числа
input_data = input("Введите целые числа через пробел: ").split()
numbers = []
for part in input_data:
    numbers.append(int(part))

result_list = []
for number in numbers:
    if 10 <= number <= 20:
        result_list.append(number)

count_val = len(result_list)
sum_val = sum(result_list)
sorted_copy = sorted(result_list)

print(f"Выборка в исходном виде: {result_list}")
print(f"Количество: {count_val}")
print(f"Сумма: {sum_val}")
print(f"Отсортированная структура: {sorted_copy}")