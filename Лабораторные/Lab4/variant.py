# Запрашиваем количество чисел

n = int(input("Введите количество чисел n: "))

# Инициализируем накопители нулями

count_suitable = 0
sum_suitable = 0

# Одним циклом запрашиваем числа и сразу проверяем условие

for i in range(1, n + 1):
    number = int(input(f"Введите число {i}: "))
    
    # Условие для 8 варианта: модуль числа больше 5

    if abs(number) > 5:
        count_suitable += 1
        sum_suitable += number

# Вывод результатов

print(f"Количество чисел с модулем > 5: {count_suitable}")
print(f"Сумма этих чисел: {sum_suitable}")