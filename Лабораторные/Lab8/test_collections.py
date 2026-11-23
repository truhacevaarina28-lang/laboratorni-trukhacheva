from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
)

#Проверка частот слов
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}

# Проверка множеств

t1 = ["python", "sql", "python"]
t2 = ["sql", "git"]
assert common_topics(t1, t2) == ["sql"]
assert all_topics(t1, t2) == ["git", "python", "sql"]
assert common_topics([], t2) == []
assert all_topics([], t2) == ["git", "sql"]

#Проверка варианта 8 на контрольном примере из задания

sample_records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]

# Сохраняем копию 

records_copy = [record.copy() for record in sample_records]

assert totals_by_category(sample_records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(sample_records, "основное") == ["A", "C"]
assert titles_in_category(sample_records, "неизвестная") == []
assert totals_by_category([]) == {}

# Проверяем, что функции не испортили исходные данные

assert sample_records == records_copy

print("Все проверки Лабораторной работы №8 успешно пройдены!")