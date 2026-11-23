import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def fetch_profile(login):
    """Получает профиль пользователя GitHub по API."""
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-course-lab11",
    })
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data


def show_profile(data):
    """Единая функция вывода профиля для обоих источников."""
    print("\n=== Данные профиля ===")
    print(f"Логин: {data.get('login')}")
    print(f"ID: {data.get('id')}")
    print(f"Имя: {data.get('name')}")


def main():
    folder = Path(__file__).resolve().parent
    choice = input("Выберите источник (1 - сеть GitHub, 2 - локальный пример): ").strip()

    if choice == "2":
        sample_path = folder / "profile_sample.json"
        try:
            with open(sample_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            print("Используются локальные данные из profile_sample.json.")
            show_profile(data)
        except (FileNotFoundError, json.JSONDecodeError, OSError) as err:
            print(f"Ошибка чтения локального файла: {err}")
        return

    try:
        data = fetch_profile(input("Логин GitHub (например, octocat): "))
        output = folder / "profile.json"
        with open(output, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"Профиль сохранён в profile.json: {data['login']}")
        show_profile(data)
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
