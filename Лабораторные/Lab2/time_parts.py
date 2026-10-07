# запрос данных 

total_seconds = int(input("Введите количество секунд: "))

# Счёт данных без остатка

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Вывод 

print(f"Результат: {hours} ч {minutes} мин {seconds} с")
