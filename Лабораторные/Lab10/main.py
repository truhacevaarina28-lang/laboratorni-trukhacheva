from pathlib import Path
from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums


def read_positive_integer(prompt_text):
    """Задание 1: надежный ввод целого положительного числа."""
    while True:
        user_input = input(prompt_text)
        try:
            number = int(user_input)
        except ValueError:
            print("Ошибка: нужно ввести целое число")
            continue

        if number <= 0:
            print("Ошибка: число должно быть больше нуля")
            continue

        return number


def main():
    # Демонстрация Задания 1
    print("=== Задание 1: Проверка ввода числа ===")
    test_num = read_positive_integer("Введите любое целое положительное число: ")
    print(f"Принято корректное число: {test_num}\n")

    # Настраиваем пути к файлам в папке со скриптом
    folder = Path(__file__).resolve().parent
    input_path = folder / "matrix.txt"
    report_path = folder / "report.txt"

    print("=== Задание 2 и 3: Чтение матрицы и запись отчета ===")
    # Читаем и проверяем входной файл
    try:
        matrix = read_matrix(input_path)
    except FileNotFoundError:
        print("Ошибка: входной файл matrix.txt не найден!")
        return
    except UnicodeError:
        print("Ошибка: неверная кодировка файла (требуется UTF-8)!")
        return
    except ValueError as err:
        print(f"Ошибка формата данных в файле: {err}")
        return
    except OSError as err:
        print(f"Ошибка доступа к файлу: {err}")
        return

    # Выводим размеры прочитанной матрицы
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    print(f"Успешно прочитана матрица размером {rows_count}x{cols_count}.")

    r_sums = row_sums(matrix)
    c_sums = column_sums(matrix)
    var_result = selected_sum(matrix)

    # Формируем текст отчета

    r_sums_str = " ".join(str(x) for x in r_sums)
    c_sums_str = " ".join(str(x) for x in c_sums)

    report_lines = [
        f"Суммы строк: {r_sums_str}\n",
        f"Суммы столбцов: {c_sums_str}\n",
        f"Результат варианта: {var_result}\n",
    ]

    # Записываем отчет только после успешной проверки всех данны

    try:
        with open(report_path, "w", encoding="utf-8") as report_file:
            report_file.writelines(report_lines)
        print("Отчет успешно сохранен в файл report.txt!")
    except OSError as err:
        print(f"Ошибка при сохранении отчета: {err}")


if __name__ == "__main__":
    main()