text = input("Введите текст: ")

# Разбиваем строку на слова по пробелам

words = text.split()

# счетчик для количества подходящих слов

suitable_count = 0

# Перебор каждого слова циклом

for word in words:

    # Очищаем слово от знаков препинания с краев и приводим к нижнему регистру

    cleaned_word = word.strip(".,!?;:").lower()
    
    if len(cleaned_word) == 0:
        continue
        
    if cleaned_word.count("а") == 1:
        print(cleaned_word)
        suitable_count += 1

# Проверяем, нашлись ли подходящие слова

if suitable_count == 0:
    print("Нет совпадений")
    print("Количество: 0")
else:
    print(f"Общее количество: {suitable_count}")