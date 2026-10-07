# Ввод данных для первого 

subject1 = input("Введите название первого предмета: ")
lessons1 = int(input(f"Сколько занятий в неделю по предмету {subject1}? "))
duration1 = int(input("Продолжительность одного занятия (в минутах): "))

# Ввод данных для второго 

subject2 = input("Введите название второго предмета: ")
lessons2 = int(input(f"Сколько занятий в неделю по предмету {subject2}? "))
duration2 = int(input("Продолжительность одного занятия (в минутах): "))

# Ввод доступного времени 

available_hours = float(input("Сколько всего часов доступно на неделю? "))

# Счёт минут

time_sub1 = lessons1 * duration1
time_sub2 = lessons2 * duration2

# Общая нагрузка

total_minutes = time_sub1 + time_sub2
total_hours = total_minutes / 60

# Остаток свободного времени и нагрузка за месяц (4 недели)

free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

# Вывод результатов

print("\n=== РАСЧЕТ НАГРУЗКИ ===")
print(f"Время на {subject1}: {time_sub1} мин.")
print(f"Время на {subject2}: {time_sub2} min.")
print(f"Общая нагрузка в минутах: {total_minutes} мин.")
print(f"Общая нагрузка в часах: {total_hours:.2f} ч.")
print(f"Остаток свободного времени: {free_hours:.2f} ч.")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} ч.")
