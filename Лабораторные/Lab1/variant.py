# Запрос общей информации

order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

#Малые фотографии

pos1_name = "Малые фотографии"
print(f"\nДанные для позиции: {pos1_name}")
pos1_count = int(input("Количество (шт): "))
pos1_price = float(input("Цена за единицу (руб): "))

#Большие фотографии

pos2_name = "Большие фотографии"
print(f"\nДанные для позиции: {pos2_name}")
pos2_count = int(input("Количество (шт): "))
pos2_price = float(input("Цена за единицу (руб): "))

# Доставка и оплата

delivery_cost = float(input("\nСтоимость доставки (руб): "))
money_paid = float(input("Внесенная сумма денег (руб): "))

# Расчеты

cost1 = pos1_count * pos1_price
cost2 = pos2_count * pos2_price
total_goods_cost = cost1 + cost2
total_order_cost = total_goods_cost + delivery_cost
total_items = pos1_count + pos2_count
change = money_paid - total_order_cost

#вывод чека

print(f"\n=== ЗАКАЗ: {order_name} ===")
print(f"Заказчик: {customer_name}")
print("---------------------------------------------")
print("Название | Количество | Цена | Стоимость")
print(f"{pos1_name} | {pos1_count} | {pos1_price:.2f} | {cost1:.2f}")
print(f"{pos2_name} | {pos2_count} | {pos2_price:.2f} | {cost2:.2f}")
print("---------------------------------------------")
print(f"Стоимость товаров без доставки: {total_goods_cost:.2f} руб.")
print(f"Общая сумма с доставкой: {total_order_cost:.2f} руб.")
print(f"Общее количество единиц: {total_items} шт.")
print(f"Сдача: {change:.2f} руб.")