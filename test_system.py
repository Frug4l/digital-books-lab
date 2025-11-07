# Тестирование работы с JSON и XML
from file_work import AdvancedFileWorker


def main():
    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ С ФАЙЛАМИ ===\n")

    # Создаем сложные файлы
    print("1. СОЗДАЕМ ФАЙЛЫ:")
    AdvancedFileWorker.create_complex_json()
    AdvancedFileWorker.create_complex_xml()

    print("\n2. ЧИТАЕМ ФАЙЛЫ:")
    # Читаем и показываем содержимое
    json_data = AdvancedFileWorker.read_complex_json()
    xml_data = AdvancedFileWorker.read_complex_xml()

    print("\n3. ИНФОРМАЦИЯ О ФАЙЛАХ:")
    if json_data:
        books_count = len(json_data["магазин_книг"]["книги"])
        clients_count = len(json_data["магазин_книг"]["клиенты"])
        print(f"JSON: {books_count} книг, {clients_count} клиентов")

    print("XML: проверьте файл complex_books.xml вручную")

    print("\n=== ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА ===")


if __name__ == "__main__":
    main()