# Запрос входных данных

total_tasks = int(input("Введите общее количество заданий: "))
tasks_per_pack = int(input("Введите количество заданий в одном комплекте: "))

#Количество полностью заполненных комплектов

full_packs = total_tasks // tasks_per_pack

#Остаток заданий, которые не вошли в комплект

remaining_tasks = total_tasks % tasks_per_pack

#Минимальное число комплектов

min_packs = (total_tasks + tasks_per_pack - 1) // tasks_per_pack

min_packs_final = min_packs * (total_tasks > 0)

# Вывод

print(f"\nКоличество полностью заполненных комплектов: {full_packs}")
print(f"Остаток заданий: {remaining_tasks}")
print(f"Минимальное число комплектов для всех заданий: {min_packs_final}")
