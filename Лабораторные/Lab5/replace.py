# Ввод текста

text = input("Введите текст с двоеточиями: ")

# Сначала считаем сколько двоеточий в исходном тексте

colons_count = text.count(":")

#делаем замену
new_text = text.replace(":", "-")

#Вывод результата

print(f"Количество замен: {colons_count}")
print(f"Новая строка: {new_text}")