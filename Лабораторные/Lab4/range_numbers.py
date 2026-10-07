# Вводим границы

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Если a меньше b, идем по возрастанию

if a < b:
    for i in range(a, b + 1):
        print(i)

# Если a больше b, идем по убыванию (шаг -1)

elif a > b:
    for i in range(a, b - 1, -1):
        print(i)
# Если они равны, просто выводим одно число

else:
    print(a)
