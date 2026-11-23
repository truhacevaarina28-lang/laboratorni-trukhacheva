from logic import (
    validate_records,
    add_record,
    find_records,
    set_completed,
    delete_record,
    statistics,
)

# 1. Проверка пустого списка и статистики
recs = []
st_empty = statistics(recs)
assert st_empty["total"] == 0
assert st_empty["total_amount"] == 0

# 2. Добавление записей (включая одинаковые названия и обрезку пробелов)
r1 = add_record(recs, "  Тропа в горах  ", " горы ", 12)
r2 = add_record(recs, "Тропа в горах", "лес", 8)
assert r1["id"] == 1 and r1["title"] == "Тропа в горах"
assert r2["id"] == 2

# 3. Изменение статуса и поиск без учёта регистра
assert set_completed(recs, 2, True) is True
assert set_completed(recs, 999, True) is False

found = find_records(recs, "ТРОПА")
assert len(found) == 2

# 4. Статистика по нескольким категориям
st = statistics(recs)
assert st["total"] == 2
assert st["completed"] == 1
assert st["uncompleted"] == 1
assert st["total_amount"] == 20
assert st["by_category"] == {"горы": 12, "лес": 8}

# 5. Удаление записи с ID 1 и проверка следующего ID (должен стать 3)
assert delete_record(recs, 1) is True
assert delete_record(recs, 1) is False
assert recs[0]["id"] == 2

r3 = add_record(recs, "Речной маршрут", "вода", 30)
assert r3["id"] == 3

# 6. Проверка строгих типов в validate_records
bad_data = [
    [{"id": True, "title": "А", "category": "Б", "amount": 10, "completed": False}],  # id = bool
    [{"id": 1, "title": "А", "category": "Б", "amount": True, "completed": False}],  # amount = bool
    [{"id": 1, "title": "А", "category": "Б", "amount": -5, "completed": False}],    # amount < 0
    [{"id": 1, "title": "А", "category": "Б", "amount": 10, "completed": "false"}],  # completed str
    [{"id": 1, "title": " ", "category": "Б", "amount": 10, "completed": False}],    # пустой title
    [{"id": 1, "title": "А", "category": "Б", "amount": 10, "completed": False},
     {"id": 1, "title": "В", "category": "Б", "amount": 5, "completed": True}],      # дубль id
]

for bad in bad_data:
    try:
        validate_records(bad)
    except ValueError:
        pass
    else:
        assert False, f"Ошибка валидации не сработала для: {bad}"

print("Все тесты logic.py пройдены успешно!")
