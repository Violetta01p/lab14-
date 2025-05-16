# Пошук записів у щоденнику за словом або датою

# Користувач вводить слово або дату для пошуку
search = input("Введіть слово або дату для пошуку: ").lower()

# Відкриваємо щоденник для читання
with open("diary.txt", "r", encoding="utf-8") as file:
    entries = file.read().split("-" * 40 + "\n")  # розділяємо записи

# Перевіряємо, чи є записи з цим словом або датою
found = False
for entry in entries:
    if search in entry.lower():
        print("\nЗнайдено запис:")
        print(entry.strip())
        found = True

if not found:
    print("Записів не знайдено.")
