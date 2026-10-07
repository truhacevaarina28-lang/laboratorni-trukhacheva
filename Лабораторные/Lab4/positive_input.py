# Счетчик неправ попыток

rejected_attempts = 0

#  бесконечный цикл для проверки

while True:
    num = int(input("Введите положительное число: "))
    
    # Если число положительное — прерываем цикл

    if num > 0:
        break
        
    # Если ноль или отрицательное — считаем ошибку

    rejected_attempts += 1

# Считаем квадрат правильного числа

square_result = num ** 2

print(f"Квадрат числа: {square_result}")
print(f"Количество отклонённых попыток: {rejected_attempts}")
