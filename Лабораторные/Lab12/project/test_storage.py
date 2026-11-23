from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records

with TemporaryDirectory() as tmp_dir:
    file_path = Path(tmp_dir) / "test_data.json"

    # 1. Если файла нет — возвращается пустой список
    assert load_records(file_path) == []

    # 2. Сохранение и повторная загрузка
    sample = [
        {"id": 1, "title": "Маршрут 1", "category": "горы", "amount": 25, "completed": True},
        {"id": 2, "title": "Маршрут 2", "category": "лес", "amount": 10, "completed": False},
    ]
    save_records(file_path, sample)
    loaded = load_records(file_path)
    assert loaded == sample

    # 3. Повреждённый JSON вызывает ошибку при чтении
    bad_file = Path(tmp_dir) / "broken.json"
    bad_file.write_text("{broken json", encoding="utf-8")
    try:
        load_records(bad_file)
    except Exception:
        pass
    else:
        assert False, "Не выброшена ошибка на битый JSON"

print("Все тесты storage.py пройдены успешно!")
