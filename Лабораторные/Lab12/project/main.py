import json
from pathlib import Path
from logic import (
    add_record,
    find_records,
    set_completed,
    delete_record,
    statistics,
)
from storage import load_records, save_records


def read_non_empty(prompt):
    """Запрашивает непустую строку."""
    while True:
        text = input(prompt).strip()
        if len(text) > 0:
            return text
        print("Ошибка: ввод не должен быть пустым.")


def read_int(prompt, min_value=None):
    """Запрашивает целое число с проверкой минимальной границы."""
    while True:
        raw = input(prompt).strip()
        try:
            num = int(raw)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue

        if min_value is not None and num < min_value:
            print(f"Ошибка: число должно быть не меньше {min_value}.")
            continue
        return num


def print_records(records):
    """Красиво выводит список маршрутов по возрастанию ID."""
    if len(records) == 0:
        print("Нет записей.")
        return

    sorted_recs = sorted(records, key=lambda item: item["id"])
    print("\nID | Название маршрута | Категория | Длина (км) | Статус")
    print("-" * 65)
    for rec in sorted_recs:
        status_text = "пройден" if rec["completed"] else "не пройден"
        print(f"{rec['id']} | {rec['title']} | {rec['category']} | {rec['amount']} км | {status_text}")


def show_menu():
    print("\n=== ПЛАН ТУРИСТИЧЕСКИХ МАРШРУТОВ ===")
    print("1. Показать все маршруты")
    print("2. Добавить маршрут")
    print("3. Найти маршруты по названию")
    print("4. Изменить статус маршрута")
    print("5. Удалить маршрут")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("0. Выйти")


def main():
    folder = Path(__file__).resolve().parent
    data_path = folder / "data.json"

    # Загрузка при старте
    if not data_path.exists():
        print("Файл data.json не найден. Начинаем работу с пустого списка.")
        records = []
    else:
        try:
            records = load_records(data_path)
            print(f"Загружено маршрутов: {len(records)}")
        except UnicodeError:
            print("Критическая ошибка: неверная кодировка файла data.json (нужна UTF-8).")
            return
        except json.JSONDecodeError as err:
            print(f"Критическая ошибка: повреждённый JSON ({err}). Файл не изменён.")
            return
        except ValueError as err:
            print(f"Критическая ошибка структуры данных: {err}. Файл не изменён.")
            return
        except OSError as err:
            print(f"Критическая ошибка чтения файла: {err}")
            return

    # Основной цикл меню
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            print_records(records)

        elif choice == "2":
            title = read_non_empty("Введите название маршрута: ")
            category = read_non_empty("Введите категорию (например, горы, лес, вода): ")
            km = read_int("Введите длину в целых километрах (>= 0): ", min_value=0)
            created = add_record(records, title, category, km)
            print(f"Маршрут добавлен с ID = {created['id']}.")

        elif choice == "3":
            query = read_non_empty("Введите текст для поиска в названии: ")
            found = find_records(records, query)
            if len(found) == 0:
                print("По вашему запросу ничего не найдено.")
            else:
                print_records(found)

        elif choice == "4":
            if len(records) == 0:
                print("Список маршрутов пуст.")
                continue
            rec_id = read_int("Введите ID маршрута: ", min_value=1)
            print("Выберите новый статус: 1 — пройден, 2 — не пройден")
            st_choice = input("Ваш выбор: ").strip()
            if st_choice == "1":
                new_status = True
            elif st_choice == "2":
                new_status = False
            else:
                print("Неверный выбор статуса. Изменения отменены.")
                continue

            if set_completed(records, rec_id, new_status):
                print("Статус маршрута успешно обновлён.")
            else:
                print(f"Маршрут с ID = {rec_id} не найден.")

        elif choice == "5":
            if len(records) == 0:
                print("Список маршрутов пуст.")
                continue
            rec_id = read_int("Введите ID маршрута для удаления: ", min_value=1)
            confirm = input(f"Вы уверены, что хотите удалить маршрут ID={rec_id}? (введите 'да' для подтверждения): ").strip().lower()
            if confirm == "да":
                if delete_record(records, rec_id):
                    print("Маршрут удалён.")
                else:
                    print(f"Маршрут с ID = {rec_id} не найден.")
            else:
                print("Удаление отменено.")

        elif choice == "6":
            stats = statistics(records)
            print("\n=== Статистика маршрутов ===")
            print(f"Всего маршрутов: {stats['total']}")
            print(f"Пройдено: {stats['completed']}")
            print(f"Не пройдено: {stats['uncompleted']}")
            print(f"Общая длина всех маршрутов: {stats['total_amount']} км")
            print("Километраж по категориям:")
            if len(stats["by_category"]) == 0:
                print("  (нет данных)")
            else:
                for cat in sorted(stats["by_category"]):
                    print(f"  {cat}: {stats['by_category'][cat]} км")

        elif choice == "7":
            try:
                save_records(data_path, records)
                print("Данные успешно сохранены в data.json!")
            except OSError as err:
                print(f"Ошибка при сохранении файла: {err}")

        elif choice == "0":
            while True:
                ans = input("Сохранить изменения перед выходом? (да / нет): ").strip().lower()
                if ans == "да":
                    try:
                        save_records(data_path, records)
                        print("Данные сохранены. Выход из программы.")
                        return
                    except OSError as err:
                        print(f"Не удалось сохранить данные ({err}). Возврат в меню.")
                        break
                elif ans == "нет":
                    print("Выход без сохранения.")
                    return
                else:
                    print("Пожалуйста, введите ровно 'да' или 'нет'.")
        else:
            print("Неизвестная команда. Выберите пункт из меню.")


if __name__ == "__main__":
    main()
