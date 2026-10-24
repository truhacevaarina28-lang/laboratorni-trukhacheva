from functions import sum_digits, average, normalize_text, select_numbers

def main():
    print("--- Тестирование функций ---")
    
    # 1. Проверка суммы цифр

    num = int(input("Введите целое число для подсчета суммы цифр: "))
    print(f"Сумма цифр: {sum_digits(num)}")
    
    input_data = input("\nВведите числа для списка через пробел: ").split()
    numbers = []
    for part in input_data:
        numbers.append(int(part))
        
    avg_result = average(numbers)
    if avg_result is None:
        print("Среднее значение: Нет данных")
    else:
        print(f"Среднее значение: {avg_result:.2f}")
        
    user_text = input("\nВведите произвольный текст: ")
    print(f"Нормализованный текст: '{normalize_text(user_text)}'")
    
    print("\n--- Индивидуальный вариант 8 (Модуль не больше порога) ---")
    if len(numbers) == 0:
        print("Исходный список пуст.")
    else:
        threshold = int(input("Введите неотрицательный порог: "))
        
        original_copy = numbers.copy()
        
        filtered_list = select_numbers(numbers, threshold)
        
        print(f"Результат отбора: {filtered_list}")
        print(f"Исходный список остался цел: {numbers == original_copy}")

if __name__ == "__main__":
    main()