from table import row_sums, column_sums, diagonal_pattern, transform

# 1. Проверка прямоугольной матрицы 2x3
m1 = [[1, 2, 3], [4, 5, 6]]
assert row_sums(m1) == [6, 15]
assert column_sums(m1) == [5, 7, 9]

# 2. Проверка матрицы из одного элемента 1x1
m2 = [[7]]
assert row_sums(m2) == [7]
assert column_sums(m2) == [7]
assert diagonal_pattern(1) == [list((0,))]

# 3. Проверка матрицы-столбца 3x1
m3 = [[1], [-1], [0]]
assert row_sums(m3) == [1, -1, 0]
assert column_sums(m3) == [0]

# 4. Проверка пустой матрицы
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# 5. Проверка диагонального узора размера 3
expected_pattern = [
    list((0, 1, 1)),
    list((2, 0, 1)),
    list((2, 2, 0))
]
assert diagonal_pattern(3) == expected_pattern

# 6. Проверка Варианта 8 (Отрицательные уменьшить на 2)
source = [[-2, 0, 3], [4, -5, 6]]
expected_transformed = [[-4, 0, 3], [4, -7, 6]]

result = transform(source)
assert result == expected_transformed

# 7. Проверка независимости копии (меняем результат и смотрим, что исходник цел)
result[0][0] = 999
assert source == [[-2, 0, 3], [4, -5, 6]], "Ошибка: исходная матрица изменилась!"

print("Все проверки Лабораторной работы №9 успешно пройдены!")
