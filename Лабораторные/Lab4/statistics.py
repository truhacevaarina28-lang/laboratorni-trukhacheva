# Запрос количества чисел

n = int(input("Сколько чисел будете вводить? "))

# Вводим первое число отдельно

first_num = int(input("Введите число 1: "))

total_sum = first_num
max_value = first_num

# Считаем положительные числа

if first_num > 0:
    positive_count = 1
else:
    positive_count = 0

# В цикле запрашиваем оставшиеся n - 1 чисел

for i in range(2, n + 1):
    current_num = int(input(f"Введите число {i}: "))
    
    #накоп сумма

    total_sum += current_num
    
    #положительные

    if current_num > 0:
        positive_count += 1
        
    #максимум

    if current_num > max_value:
        max_value = current_num

#итоги

print(f"Сумма: {total_sum}")
print(f"Количество положительных: {positive_count}")
print(f"Максимум: {max_value}")
