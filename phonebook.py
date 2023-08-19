import os


DATA_FILE = "phonebook.csv"

# Создание файла данных, если он не существует
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        file.write("Фамилия,Имя,Отчество,Организация,Рабочий телефон,Личный телефон\n")


def read_data(file_name):
    data = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            entry = line.strip().split(',')
            data.append(entry)
    return data


def write_data(file_name, data):
    with open(file_name, "w") as file:
        file.write("Фамилия,Имя,Отчество,Организация,Рабочий телефон,Личный телефон\n")
        for entry in data:
            file.write(','.join(entry) + '\n')


def display_entries(entries):
    for entry in entries:
        print("Фамилия:", entry[0])
        print("Имя:", entry[1])
        print("Отчество:", entry[2])
        print("Организация:", entry[3])
        print("Рабочий телефон:", entry[4])
        print("Личный телефон:", entry[5])
        print("=" * 40)


def add_entry(data):
    new_entry = []
    new_entry.append(input("Фамилия: "))
    new_entry.append(input("Имя: "))
    new_entry.append(input("Отчество: "))
    new_entry.append(input("Организация: "))
    new_entry.append(input("Рабочий телефон: "))
    new_entry.append(input("Личный телефон: "))
    data.append(new_entry)
    write_data(DATA_FILE, data)
    print("Запись успешно добавлена!")


def edit_entry(data, index):
    if 0 <= index < len(data):
        entry = data[index]
        print("Текущая запись:")
        display_entries([entry])
        print("=" * 40)
        field = int(input("Выберите поле для редактирования (1-6): "))
        if 1 <= field <= 6:
            entry[field - 1] = input("Новое значение: ")
            write_data(DATA_FILE, data)
            print("Запись успешно отредактирована!")
        else:
            print("Недопустимое поле.")
    else:
        print("Недопустимый индекс записи.")


def search_entries(data, search_terms):
    results = []
    for entry in data:
        for term in search_terms:
            if any(term.lower() in field.lower() for field in entry):
                results.append(entry)
                break
    return results


def main():
    data = read_data(DATA_FILE)

    while True:
        print("\nТелефонный справочник")
        print("1. Вывести записи")
        print("2. Добавить новую запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_entries(data)
        elif choice == "2":
            add_entry(data)
        elif choice == "3":
            index = int(input("Введите индекс записи для редактирования: "))
            edit_entry(data, index)
        elif choice == "4":
            search_terms = input("Введите поисковые термины (через запятую): ").split(',')
            search_results = search_entries(data, search_terms)
            if search_results:
                display_entries(search_results)
            else:
                print("Нет результатов поиска.")
        elif choice == "5":
            break
        else:
            print("Недопустимый выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
