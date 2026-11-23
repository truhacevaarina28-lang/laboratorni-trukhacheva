import json
from pathlib import Path
from analysis import (
    validate_todos,
    completion_counts,
    top_users,
    get_leader_tasks,
    select_tasks,
)


def read_positive_int(prompt):
    """Надёжный запрос положительного целого числа."""
    while True:
        raw = input(prompt)
        try:
            val = int(raw)
        except ValueError:
            print("Ошибка: нужно ввести целое число")
            continue
        if val <= 0:
            print("Ошибка: число должно быть больше нуля")
            continue
        return val


def read_non_empty_text(prompt):
    """Запрос непустой текстовой подстроки (параметр для Варианта 8)."""
    while True:
        text = input(prompt).strip()
        if len(text) == 0:
            print("Ошибка: подстрока не должна быть пустой")
            continue
        return text


def main():
    folder = Path(__file__).resolve().parent
    input_path = folder / "todos.json"
    leaders_path = folder / "leaders.json"
    selected_path = folder / "selected.json"

    # 1. Чтение и проверка входного JSON
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            todos = json.load(file)
        validate_todos(todos)
    except FileNotFoundError:
        print("Ошибка: файл todos.json не найден!")
        return
    except UnicodeError:
        print("Ошибка: неверная кодировка файла (нужна UTF-8)!")
        return
    except json.JSONDecodeError as err:
        print(f"Ошибка синтаксиса JSON: {err}")
        return
    except ValueError as err:
        print(f"Ошибка структуры данных: {err}")
        return
    except OSError as err:
        print(f"Ошибка доступа к файлу: {err}")
        return

    # 2. Анализ лидеров
    counts = completion_counts(todos)
    leaders = top_users(counts)
    leader_tasks = get_leader_tasks(todos, leaders)

    print("=== Сводка по задачам ===")
    print("Выполнено задач по пользователям:", counts)
    print("Лидеры по выполненным задачам:", leaders)

    # 3. Запрос параметров для Варианта 8
    print("\n=== Поиск задач пользователя по подстроке (Вариант 8) ===")
    target_user = read_positive_int("Введите положительный user_id (например, 5): ")
    substring = read_non_empty_text("Введите подстроку для поиска в названии (например, и): ")

    selected = select_tasks(todos, target_user, substring)
    print(f"Найдено задач: {len(selected)}")

    # 4. Сохранение результатов в JSON-файлы
    try:
        with open(leaders_path, "w", encoding="utf-8") as f_lead:
            json.dump(leader_tasks, f_lead, ensure_ascii=False, indent=2)

        with open(selected_path, "w", encoding="utf-8") as f_sel:
            json.dump(selected, f_sel, ensure_ascii=False, indent=2)

        print("Результаты успешно сохранены в leaders.json и selected.json!")
    except OSError as err:
        print(f"Ошибка при сохранении результатов: {err}")


if __name__ == "__main__":
    main()