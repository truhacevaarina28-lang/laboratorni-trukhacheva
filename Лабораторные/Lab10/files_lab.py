def read_matrix(path):

    """Читает матрицу из файла и проверяет корректность формата."""
    with open(path, "r", encoding="utf-8") as file:

        # Читаем все строки и убираем перенос строки на конце

        raw_lines = file.readlines()

    # Убираем пустые переводы в самом конце файла, но сохраняем пустые строки в середине для проверки

    lines = []
    for line in raw_lines:
        lines.append(line.rstrip("\r\n"))

    # Если в самом конце была одна пустая строка от Enter, убираем её

    if len(lines) > 0 and lines[-1] == "":
        lines.pop()

    if len(lines) == 0:
        raise ValueError("Файл пуст")

    # Проверяем первую строку 

    header_parts = lines[0].split()
    if len(header_parts) != 2:
        raise ValueError("Строка 1: ожидалось два целых числа (строки и столбцы)")

    try:
        rows = int(header_parts[0])
        cols = int(header_parts[1])
    except ValueError:
        raise ValueError("Строка 1: размеры таблицы должны быть целыми числами")

    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: размеры таблицы должны быть больше нуля")

    # Проверяем, совпадает ли 

    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(f"Ожидалось строк данных: {rows}, но в файле найдено: {len(data_lines)}")

    matrix = []

    # Перебираем строки с данными
    
    for i in range(len(data_lines)):
        line_num = i + 2  # Номер строки в файле для понятной ошибки
        line_text = data_lines[i].strip()

        if len(line_text) == 0:
            raise ValueError(f"Строка {line_num}: обнаружена пустая строка")

        parts = line_text.split()
        if len(parts) != cols:
            raise ValueError(f"Строка {line_num}: ожидалось чисел: {cols}, получено: {len(parts)}")

        row = []
        for part in parts:
            try:
                num = int(part)
                row.append(num)
            except ValueError:
                raise ValueError(f"Строка {line_num}: значение '{part}' не является целым числом")

        matrix.append(row)

    return matrix


def selected_sum(matrix):
    """Вариант 8: сумма элементов первой строки матрицы."""
    if len(matrix) == 0:
        return 0
    return sum(matrix[0])
