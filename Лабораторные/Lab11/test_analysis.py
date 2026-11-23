import json
from pathlib import Path
from tempfile import TemporaryDirectory
from analysis import (
    validate_todos,
    completion_counts,
    top_users,
    get_leader_tasks,
    select_tasks,
)

# 1. Учебный набор из условия
sample_todos = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]

validate_todos(sample_todos)
counts = completion_counts(sample_todos)
assert counts == {5: 2, 10: 2}

leaders = top_users(counts)
assert leaders == [5, 10]

leader_tasks = get_leader_tasks(sample_todos, leaders)
leader_ids = [t["id"] for t in leader_tasks]
assert leader_ids == [1, 3, 4, 5]

# 2. Пустой список и набор только с completed=False
assert completion_counts([]) == {}
assert top_users({}) == []

no_completed = [
    {"id": 1, "userId": 1, "title": "Задача", "completed": False}
]
c_zero = completion_counts(no_completed)
assert c_zero == {1: 0}
assert top_users(c_zero) == []
assert get_leader_tasks(no_completed, []) == []

# 3. Один лидер
assert top_users({1: 3, 2: 1}) == [1]

# 4. Индивидуальный вариант 8 (Поиск по подстроке без учёта регистра)
# Контрольный пример: user_id=5, подстрока "и" -> id [2, 5]
res_var = select_tasks(sample_todos, 5, "и")
assert [t["id"] for t in res_var] == [2, 5]

# Проверка смешанного регистра
res_case = select_tasks(sample_todos, 5, "СПИС")
assert [t["id"] for t in res_case] == [5]

# Неизвестный пользователь и отсутствие совпадений
assert select_tasks(sample_todos, 999, "и") == []
assert select_tasks(sample_todos, 5, "несуществующее") == []

# 5. Проверки ошибок валидации 
bad_cases = [
    "не список",
    [{"id": 1, "userId": 5, "title": 123, "completed": True}],           # title не строка
    [{"id": 1, "userId": 5, "title": "А", "completed": True},
     {"id": 1, "userId": 5, "title": "Б", "completed": True}],          # дубликат id
    [{"id": 1, "title": "А", "completed": True}],                       # нет userId
    [{"id": 1, "userId": 5, "title": "А", "completed": "false"}],       # completed строка
    [{"id": True, "userId": 5, "title": "А", "completed": True}],       # id = bool
]

for bad in bad_cases:
    try:
        validate_todos(bad)
    except ValueError:
        pass
    else:
        assert False, f"Ошибка валидации не сработала для: {bad}"

# 6. Проверка записи и повторного чтения JSON
with TemporaryDirectory() as tmp:
    file_path = Path(tmp) / "out.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(res_var, f, ensure_ascii=False, indent=2)
    with open(file_path, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    assert reloaded == res_var

print("Все проверки Лабораторной работы №11 успешно пройдены!")
