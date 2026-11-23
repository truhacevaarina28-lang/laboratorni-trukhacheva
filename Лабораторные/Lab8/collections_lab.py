def word_counts(text):
    """Считает, сколько раз каждое слово встречается в тексте."""
    counts = {}
    words = text.split()
    
    for word in words:
        # Очищаем слово от знаков препинания делаем нижний регистр
        cleaned = word.strip(".,!?;:").lower()
        
        # Если после очистки осталась пустота, пропускаем
        if len(cleaned) == 0:
            continue
            
        if cleaned not in counts:
            counts[cleaned] = 1
        else:
            counts[cleaned] += 1
            
    return counts


def common_topics(first, second):
    """Возвращает отсортированный список общих тем (пересечение множеств)."""
    set1 = set(first)
    set2 = set(second)
    common = set1 & set2
    return sorted(common)

def all_topics(first, second):
    """Возвращает отсортированный список всех уникальных тем (объединение множеств)."""
    set1 = set(first)
    set2 = set(second)
    all_unique = set1 | set2
    return sorted(all_unique)


# === Индивидуальный вариант 8: Туристические поездки (amount = целые километры) ===
def totals_by_category(records):
    """Возвращает словарь: категория -> сумма километров."""
    totals = {}
    
    for record in records:
        cat = record["category"]
        km = record["amount"]
        
        if cat not in totals:
            totals[cat] = km
        else:
            totals[cat] += km
            
    return totals

def titles_in_category(records, category):
    """Возвращает список названий поездок в указанной категории в исходном порядке."""
    result_titles = []
    
    for record in records:
        if record["category"] == category:
            result_titles.append(record["title"])
            
    return result_titles


# === Интерактивный запуск (сработает только при прямом запуске файла) ===
if __name__ == "__main__":
    print("=== Задание 1: Частоты слов ===")
    sample_text = input("Введите текст: ")
    counts = word_counts(sample_text)
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")

    print("\n=== Задание 3: Запись и пара (Кортеж) ===")

    # Создаем словарь

    course_record = {"title": "Основы Python", "hours": 10}


    course_record["hours"] = 12
    course_record["completed"] = False
    
    # Создаем кортеж из двух значений и распаковываем его
    course_pair = (course_record["title"], course_record["hours"])
    title_val, hours_val = course_pair
    print(f"Распакованная пара: название = '{title_val}', часов = {hours_val}")

    print("\n=== Вариант 8: Туристические поездки ===")

    trips = [
        {"title": "Поход на Эльбрус", "category": "горы", "amount": 45},
        {"title": "Прогулка по Казани", "category": "город", "amount": 15},
        {"title": "Сплав по реке Белой", "category": "вода", "amount": 60},
        {"title": "Восхождение на Фишт", "category": "горы", "amount": 30},
        {"title": "Экскурсия по Питеру", "category": "город", "amount": 20},
    ]

    print("Сводка по категориям (в километрах):")
    summary = totals_by_category(trips)
    for cat in sorted(summary):
        print(f"  {cat}: {summary[cat]} км")

    search_cat = input("\nВведите категорию для поиска поездок (например, горы, город, вода): ")
    found = titles_in_category(trips, search_cat)
    print(f"Найденные поездки: {found}")