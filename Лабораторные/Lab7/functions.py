def sum_digits(number):

    """Возвращает сумму цифр модуля числа."""

    num = abs(number)
    digits_sum = 0
    while num > 0:
        digits_sum += num % 10
        num = num // 10
    return digits_sum

def average(numbers):

    """Возвращает среднее значение списка"""

    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    words = text.split()
    return " ".join(words).lower()

def select_numbers(numbers, threshold):

    result = []
    for number in numbers:
        if abs(number) <= threshold:
            result.append(number)
    return result