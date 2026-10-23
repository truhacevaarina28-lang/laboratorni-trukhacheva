# Ввод строки

text = input("Введите текст для проверки на палиндром: ")

# Очистка текста от обычных пробелов и перевод в нижний регистр

cleaned_text = text.replace(" ", "").lower()

# Проверка, на пустоту строки после отчистки 

if len(cleaned_text) == 0:
    print("Нет текста")
else:
    # Разворот очищенной строки

    reversed_text = cleaned_text[::-1]
    
    # Сравниваем оригинал и перевертыш

    if cleaned_text == reversed_text:
        print("Палиндром")
    else:
        print("Не палиндром")