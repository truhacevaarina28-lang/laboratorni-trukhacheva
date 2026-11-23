import json
from pathlib import Path
from logic import validate_records


def load_records(path):
    """Загружает и проверяет маршруты из JSON. Если файла нет — возвращает пустой список."""
    file_path = Path(path)
    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    validate_records(data)
    return data


def save_records(path, records):
    """Проверяет и сохраняет список маршрутов в JSON в кодировке UTF-8."""
    validate_records(records)
    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
