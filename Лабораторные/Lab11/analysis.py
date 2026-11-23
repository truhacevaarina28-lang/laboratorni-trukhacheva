def validate_todos(data):
    """Проверяет структуру JSON-данных. При нарушении выбрасывает ValueError."""
    if not isinstance(data, list):
        raise ValueError("Корень данных должен быть списком")

    seen_ids = set()
    for i in range(len(data)):
        item = data[i]
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i}: запись должна быть словарём")

        # Проверка наличия обязательных ключей
        required_keys = ["id", "userId", "title", "completed"]
        for key in required_keys:
            if key not in item:
                raise ValueError(f"Элемент {i}: отсутствует обязательный ключ '{key}'")

        # Строгая проверка целых чисел (исключая bool)
        if type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError(f"Элемент {i}: поле 'id' должно быть положительным целым числом")
        if type(item["userId"]) is not int or item["userId"] <= 0:
            raise ValueError(f"Элемент {i}: поле 'userId' должно быть положительным целым числом")

        # Проверка уникальности id
        if item["id"] in seen_ids:
            raise ValueError(f"Элемент {i}: дублирующийся id = {item['id']}")
        seen_ids.add(item["id"])

        # Проверка непустой строки title
        if type(item["title"]) is not str or len(item["title"].strip()) == 0:
            raise ValueError(f"Элемент {i}: поле 'title' должно быть непустой строкой")

        # Строгая проверка логического значения
        if type(item["completed"]) is not bool:
            raise ValueError(f"Элемент {i}: поле 'completed' должно быть логическим (bool)")


def completion_counts(todos):
    """Возвращает словарь: userId -> количество выполненных задач (включая тех, у кого 0)."""
    counts = {}
    for task in todos:
        uid = task["userId"]
        if uid not in counts:
            counts[uid] = 0
        if task["completed"] is True:
            counts[uid] += 1
    return counts


def top_users(counts):
    """Возвращает отсортированный список userId с максимальным числом выполненных задач."""
    if len(counts) == 0:
        return []

    max_done = max(counts.values())
    if max_done == 0:
        return []

    leaders = []
    for uid, count in counts.items():
        if count == max_done:
            leaders.append(uid)

    return sorted(leaders)


def get_leader_tasks(todos, leaders):
    """Возвращает список выполненных задач пользователей-лидеров в исходном порядке."""
    leaders_set = set(leaders)
    result = []
    for task in todos:
        if task["userId"] in leaders_set and task["completed"] is True:
            result.append(task)
    return result


def select_tasks(todos, user_id, parameter=None):
    """Вариант 8: задачи пользователя user_id, в названии которых есть подстрока parameter."""
    if parameter is None:
        return []

    search_sub = parameter.strip().lower()
    if len(search_sub) == 0:
        return []

    selected = []
    for task in todos:
        if task["userId"] == user_id:
            if search_sub in task["title"].lower():
                selected.append(task)
    return selected
