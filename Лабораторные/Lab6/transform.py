# Запрашиваем и заполняем список чисел

input_data = input("Введите целые числа через пробел: ").split()
numbers = []
for part in input_data:
    numbers.append(int(part))

# Создаем новый список

transformed_numbers = []
for number in numbers:
    transformed_numbers.append(abs(number))

# Выводим оба списка

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed_numbers}")