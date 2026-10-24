from functions import average, normalize_text, sum_digits, select_numbers

# Базовый набор 

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")

test_list = [-5, 0, 2, 5]
assert select_numbers(test_list, 2) == [0, 2]

# 2. Тест с пустым списком 

assert select_numbers([], 2) == []

# 3. Проверка граничных условий и повторов

assert select_numbers([2, -2, 3, -3, 0, 2], 2) == [2, -2, 0, 2]

# 4. Проверка

source_list = [-5, 0, 2, 5]
select_numbers(source_list, 2)
assert source_list == [-5, 0, 2, 5], "Ошибка: функция изменила исходный список!"

print("Все проверки Варианта 8 успешно пройдены!")