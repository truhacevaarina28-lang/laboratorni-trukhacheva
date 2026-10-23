# Запрос исходного текста\

text = input("Введите текст для нормализации: ")

# Разбитие по пробелам и собирание обратно через один пробел

words = text.split()
normalized_text = " ".join(words)

# Счёт длины и количество слов

original_length = len(text)
new_length = len(normalized_text)
word_count = len(words)

# Вывод результатов

print(f"Исходная длина: {original_length}")
print(f"Новая длина: {new_length}")
print(f"Нормализованный текст: {normalized_text}")
print(f"Количество слов: {word_count}")