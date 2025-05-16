# Простий щоденник мандрівника

def add_note():
    # Додаємо нову нотатку у файл diary.txt
    date = input("Введіть дату (формат РРРР-ММ-ДД): ")
    location = input("Введіть локацію: ")
    text = input("Введіть текст нотатки: ")

    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"Дата: {date}\n")
        file.write(f"Локація: {location}\n")
        file.write(f"Текст: {text}\n")
        file.write("-" * 40 + "\n")  # Розділювач нотаток

    print("Нотатку додано.\n")


def search_notes():
    # Шукаємо нотатки за датою або словом
    keyword = input("Введіть дату або ключове слово для пошуку: ").lower()

    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            content = file.read().lower()
            notes = content.split("-" * 40)

            found = False
            for note in notes:
                if keyword in note:
                    print("\n--- Знайдена нотатка ---")
                    print(note.strip())
                    found = True

            if not found:
                print("Нотаток за вашим запитом не знайдено.\n")

    except FileNotFoundError:
        print("Файл щоденника не знайдено. Спочатку додайте нотатку.\n")


def analyze_notes():
    # Підрахунок нотаток, унікальних локацій і слів у файлі
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        total_notes = 0
        locations = []
        total_words = 0

        for line in lines:
            line = line.strip()

            if line.startswith("Локація:"):
                location = line.replace("Локація:", "").strip()
                locations.append(location)

            if line.startswith("Текст:"):
                text = line.replace("Текст:", "").strip()
                total_words += len(text.split())

            if line == "-" * 40:
                total_notes += 1

        print(f"\nВсього нотаток: {total_notes}")
        print(f"Унікальних локацій: {len(set(locations))}")
        print(f"Загальна кількість слів у нотатках: {total_words}\n")

    except FileNotFoundError:
        print("Файл щоденника не знайдено. Спочатку додайте нотатку.\n")


def main():
    while True:
        print("Меню:")
        print("1 - Додати нотатку")
        print("2 - Пошук нотаток")
        print("3 - Аналітика нотаток")
        print("4 - Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            search_notes()
        elif choice == "3":
            analyze_notes()
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.\n")


if __name__ == "__main__":
    main()
