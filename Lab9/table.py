def row_sums(matrix):

    """Возвращает список сумм каждой строки таблицы."""

    if len(matrix) == 0:
        return []
        
    result = []
    for row in matrix:
        result.append(sum(row))
    return result


def column_sums(matrix):

    """Возвращает список сумм каждого столбца таблицы."""

    if len(matrix) == 0:
        return []
        
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    result = []
    
    # Внешний цикл идет по столбцам, внутренний — по строкам

    for col in range(cols_count):
        col_total = 0
        for row in range(rows_count):
            col_total += matrix[row][col]
        result.append(col_total)
        
    return result


def diagonal_pattern(size):

    """Создает квадратную таблицу: 0 на диагонали, 1 выше, 2 ниже."""

    matrix = []
    for row in range(size):
        new_row = []
        for col in range(size):
            if row == col:
                new_row.append(0)
            elif row < col:
                new_row.append(1)
            else:
                new_row.append(2)
        matrix.append(new_row)
    return matrix


def transform(matrix):

    """Вариант 8: создает новую матрицу, где отрицательные числа уменьшены на 2."""

    if len(matrix) == 0:
        return []
        
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            if value < 0:
                new_row.append(value - 2)
            else:
                new_row.append(value)
        new_matrix.append(new_row)
        
    return new_matrix