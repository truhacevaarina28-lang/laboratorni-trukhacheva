from table import row_sums, column_sums, diagonal_pattern, transform

def print_matrix(matrix):
    """Вспомогательная функция для красивого вывода таблицы построчно."""
    for row in matrix:
        print(*row)

def main():
    print("=== Ввод прямоугольной таблицы ===")
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    
    matrix = []
    for i in range(rows):
        parts = input(f"Введите {columns} чисел для строки {i + 1} через пробел: ").split()
        row = []
        for p in parts:
            row.append(int(p))
            
        while len(row) != columns:
            print(f"Ошибка: нужно ввести ровно {columns} чисел!")
            parts = input("Повторите ввод строки: ").split()
            row = []
            for p in parts:
                row.append(int(p))
                
        matrix.append(row)

    print("\nИсходная таблица:")
    print_matrix(matrix)

    print("\nСуммы по строкам:", row_sums(matrix))
    print("Суммы по столбцам:", column_sums(matrix))

    print("\n=== Вариант 8: Отрицательные уменьшены на 2 ===")
    transformed = transform(matrix)
    print("Новая таблица:")
    print_matrix(transformed)

    print("\n=== Диагональный узор ===")
    size = int(input("Введите положительный размер квадратной матрицы: "))
    pattern = diagonal_pattern(size)
    print("Узор:")
    print_matrix(pattern)

if __name__ == "__main__":
    main()