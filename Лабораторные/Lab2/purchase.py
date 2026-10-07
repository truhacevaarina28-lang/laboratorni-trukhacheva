# Запрос данных 

price = int(input("Цена одной тетради: "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма: "))

# Счёт стоимости и сдачи

cost = price * count
change = paid - cost

# Итог

print(f"Стоимость покупки: {cost} руб.")
print(f"Сдача: {change} руб.")
