def validate_records(records):
    """Проверяет список записей. При нарушении правил выбрасывает ValueError."""
    if type(records) is not list:
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for i in range(len(records)):
        rec = records[i]
        if type(rec) is not dict:
            raise ValueError(f"Запись {i + 1}: элемент должен быть словарём")

        required_keys = ["id", "title", "category", "amount", "completed"]
        for key in required_keys:
            if key not in rec:
                raise ValueError(f"Запись {i + 1}: отсутствует обязательное поле '{key}'")

        # Проверка id (строго целое число > 0, не bool)
        if type(rec["id"]) is not int or rec["id"] <= 0:
            raise ValueError(f"Запись {i + 1}: 'id' должен быть положительным целым числом")
        if rec["id"] in seen_ids:
            raise ValueError(f"Запись {i + 1}: повторяющийся id = {rec['id']}")
        seen_ids.add(rec["id"])

        # Проверка title и category (непустые строки)
        if type(rec["title"]) is not str or len(rec["title"].strip()) == 0:
            raise ValueError(f"Запись {i + 1}: название маршрута должно быть непустой строкой")
        if type(rec["category"]) is not str or len(rec["category"].strip()) == 0:
            raise ValueError(f"Запись {i + 1}: категория должна быть непустой строкой")

        # Проверка amount (целое число >= 0, не bool)
        if type(rec["amount"]) is not int or rec["amount"] < 0:
            raise ValueError(f"Запись {i + 1}: длина (amount) должна быть целым числом >= 0")

        # Проверка completed (строго bool)
        if type(rec["completed"]) is not bool:
            raise ValueError(f"Запись {i + 1}: статус (completed) должен быть True или False")


def add_record(records, title, category, amount):
    """Добавляет новый маршрут в список records (изменяет список) и возвращает созданную запись."""
    clean_title = title.strip()
    clean_category = category.strip()

    if len(clean_title) == 0 or len(clean_category) == 0:
        raise ValueError("Название и категория не могут быть пустыми")
    if type(amount) is not int or amount < 0:
        raise ValueError("Длина в километрах должна быть целым неотрицательным числом")

    # Ищем максимальный текущий ID
    if len(records) == 0:
        new_id = 1
    else:
        max_id = 0
        for rec in records:
            if rec["id"] > max_id:
                max_id = rec["id"]
        new_id = max_id + 1

    new_record = {
        "id": new_id,
        "title": clean_title,
        "category": clean_category,
        "amount": amount,
        "completed": False,
    }
    records.append(new_record)
    return new_record


def find_records(records, query):
    """Ищет маршруты по подстроке в названии без учёта регистра. Не меняет исходный список."""
    clean_query = query.strip().lower()
    if len(clean_query) == 0:
        raise ValueError("Поисковый запрос не может быть пустым")

    found = []
    for rec in records:
        if clean_query in rec["title"].lower():
            found.append(rec)
    return found


def set_completed(records, record_id, completed):
    """Меняет статус прохождения маршрута по ID. Возвращает True при успехе, False если ID не найден."""
    if type(completed) is not bool:
        raise ValueError("Статус должен быть логическим значением (True/False)")

    for rec in records:
        if rec["id"] == record_id:
            rec["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет маршрут по ID. Возвращает True при успехе, False если ID не найден."""
    for i in range(len(records)):
        if records[i]["id"] == record_id:
            records.pop(i)
            return True
    return False


def statistics(records):
    """Считает статистику по текущим маршрутам. Не меняет исходный список."""
    total_count = len(records)
    completed_count = 0
    total_km = 0
    by_category = {}

    for rec in records:
        if rec["completed"] is True:
            completed_count += 1
        total_km += rec["amount"]

        cat = rec["category"].strip()
        if cat not in by_category:
            by_category[cat] = rec["amount"]
        else:
            by_category[cat] += rec["amount"]

    uncompleted_count = total_count - completed_count

    return {
        "total": total_count,
        "completed": completed_count,
        "uncompleted": uncompleted_count,
        "total_amount": total_km,
        "by_category": by_category,
    }
