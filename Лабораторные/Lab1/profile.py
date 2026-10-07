# Запраос данных 
last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")

# Возраст 
age = int(input("Введите возраст (полных лет): "))

# Часы 
study_hours = float(input("Количество часов подготовки в неделю: "))

# Счёт показателей
age_in_4_years = age + 4
hours_in_4_weeks = study_hours * 4
hours_per_day = study_hours / 7

# Вывод карточки
print("\n=== КАРТОЧКА СТУДЕНТА ===")
print(f"Студент: {first_name} {last_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст через 4 года: {age_in_4_years}")
print(f"Время подготовки за 4 недели: {hours_in_4_weeks:.2f} ч.")
print(f"Среднее время подготовки в день: {hours_per_day:.2f} ч.")
