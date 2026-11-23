from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum

with TemporaryDirectory() as directory:
    temp_dir = Path(directory)

    # 1. Базовая проверка чтения
    p1 = temp_dir / "m1.txt"
    p1.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(p1) == [list((7, -1))]

    # 2. Матрица 1x1 со значением 0
    p2 = temp_dir / "m2.txt"
    p2.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(p2) == [list((0,))]

    # 3. Пустой файл -> ValueError
    p_empty = temp_dir / "empty.txt"
    p_empty.write_text("", encoding="utf-8")
    try:
        read_matrix(p_empty)
    except ValueError:
        pass
    else:
        assert False, "Ошибка пустого файла не обнаружена"

    # 4. Заголовок 0 3 -> ValueError
    p_zero_dim = temp_dir / "zero_dim.txt"
    p_zero_dim.write_text("0 3\n", encoding="utf-8")
    try:
        read_matrix(p_zero_dim)
    except ValueError:
        pass
    else:
        assert False, "Ошибка нулевой размерности не обнаружена"

    # 5. Нехватка чисел в строке (Заголовок 1 2, строка "1") -> ValueError с номером строки 2
    p_short_row = temp_dir / "short_row.txt"
    p_short_row.write_text("1 2\n1\n", encoding="utf-8")
    try:
        read_matrix(p_short_row)
    except ValueError as err:
        assert "Строка 2" in str(err)
    else:
        assert False, "Ошибка неполной строки не обнаружена"

    # 6. Буква вместо числа (Заголовок 1 2, строка "1 x") -> ValueError с номером строки 2
    p_bad_type = temp_dir / "bad_type.txt"
    p_bad_type.write_text("1 2\n1 x\n", encoding="utf-8")
    try:
        read_matrix(p_bad_type)
    except ValueError as err:
        assert "Строка 2" in str(err)
    else:
        assert False, "Ошибка нечислового значения не обнаружена"

    # 7. Лишние строки данных (Заголовок 1 1, две строки) -> ValueError
    p_extra_rows = temp_dir / "extra_rows.txt"
    p_extra_rows.write_text("1 1\n5\n6\n", encoding="utf-8")
    try:
        read_matrix(p_extra_rows)
    except ValueError:
        pass
    else:
        assert False, "Ошибка лишних строк не обнаружена"

    # 8. Отсутствующий файл -> FileNotFoundError
    p_missing = temp_dir / "no_such_file.txt"
    try:
        read_matrix(p_missing)
    except FileNotFoundError:
        pass
    else:
        assert False, "Ошибка отсутствующего файла не обнаружена"

# 9. Проверка Варианта 8 (Сумма первой строки)
sample_m = [list((1, -2, 3)), list((4, 0, -6))]
assert selected_sum(sample_m) == 2
assert selected_sum([]) == 0

print("Все проверки Лабораторной работы №10 успешно пройдены!")
