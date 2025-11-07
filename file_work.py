# Дополнительные методы для работы с новыми файлами
import json
import xml.etree.ElementTree as ET
from datetime import datetime


class AdvancedFileWorker:
    """Расширенный работник с файлами - для новых структур"""

    @staticmethod
    def create_complex_json():
        """Создание сложного JSON файла"""
        data = {
            "магазин_книг": {
                "название": "Интернет-магазин цифровых книг",
                "версия": "1.0",
                "дата_создания": "2024",
                "книги": [
                    {
                        "ид_книги": 101,
                        "название": "Война и мир",
                        "автор": {
                            "ид_автора": 1,
                            "имя": "Толстой Л.Н.",
                            "биография": "Великий русский писатель"
                        },
                        "цена": 299.99,
                        "валюта": "руб",
                        "формат": "PDF",
                        "размер_мб": 15,
                        "рейтинг": 4.8
                    },
                    {
                        "ид_книги": 102,
                        "название": "Евгений Онегин",
                        "автор": {
                            "ид_автора": 2,
                            "имя": "Пушкин А.S.",
                            "биография": "Великий русский поэт"
                        },
                        "цена": 199.5,
                        "валюта": "руб",
                        "формат": "EPUB",
                        "размер_мб": 3,
                        "рейтинг": 4.9
                    }
                ],
                "клиенты": [
                    {
                        "ид_клиента": 1,
                        "имя": "Иванов Иван",
                        "email": "ivanov@mail.ru",
                        "дата_регистрации": "2024-01-15"
                    }
                ]
            }
        }

        try:
            with open("complex_books.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Создали сложный JSON файл: complex_books.json")
        except Exception as e:
            print(f"Ошибка при создании JSON: {e}")

    @staticmethod
    def read_complex_json():
        """Чтение сложного JSON файла"""
        try:
            with open("complex_books.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            print("\n=== ЧТЕНИЕ СЛОЖНОГО JSON ===")
            shop_info = data["магазин_книг"]
            print(f"Магазин: {shop_info['название']}")
            print(f"Книг в каталоге: {len(shop_info['книги'])}")

            for book in shop_info["книги"]:
                print(f"  - {book['название']} ({book['цена']} {book['валюта']})")

            return data

        except FileNotFoundError:
            print("Файл complex_books.json не найден!")
            return None
        except Exception as e:
            print(f"Ошибка чтения JSON: {e}")
            return None

    @staticmethod
    def create_complex_xml():
        """Создание сложного XML файла"""
        # Корневой элемент
        root = ET.Element("библиотека_цифровых_книг")
        root.set("версия", "1.0")
        root.set("дата_создания", "2024")

        # Информация о магазине
        shop_info = ET.SubElement(root, "информация_о_магазине")
        ET.SubElement(shop_info, "название").text = "Магазин цифровых книг"
        ET.SubElement(shop_info, "адрес_сайта").text = "www.books.ru"
        ET.SubElement(shop_info, "телефон").text = "8-800-123-45-67"

        # Авторы
        authors = ET.SubElement(root, "авторы")

        author1 = ET.SubElement(authors, "автор")
        ET.SubElement(author1, "ид").text = "1"
        ET.SubElement(author1, "имя").text = "Толстой Л.Н."
        ET.SubElement(author1, "страна").text = "Россия"

        author2 = ET.SubElement(authors, "автор")
        ET.SubElement(author2, "ид").text = "2"
        ET.SubElement(author2, "имя").text = "Пушкин А.С."
        ET.SubElement(author2, "страна").text = "Россия"

        # Книги
        catalog = ET.SubElement(root, "каталог_книг")

        book1 = ET.SubElement(catalog, "книга")
        book1.set("категория", "классика")
        ET.SubElement(book1, "ид").text = "101"
        ET.SubElement(book1, "название").text = "Война и мир"
        ET.SubElement(book1, "ид_автора").text = "1"
        ET.SubElement(book1, "цена").text = "299.99"
        ET.SubElement(book1, "рейтинг").text = "4.8"

        book2 = ET.SubElement(catalog, "книга")
        book2.set("категория", "поэзия")
        ET.SubElement(book2, "ид").text = "102"
        ET.SubElement(book2, "название").text = "Евгений Онегин"
        ET.SubElement(book2, "ид_автора").text = "2"
        ET.SubElement(book2, "цена").text = "199.50"
        ET.SubElement(book2, "рейтинг").text = "4.9"

        # Сохраняем XML
        tree = ET.ElementTree(root)
        tree.write("complex_books.xml", encoding="utf-8", xml_declaration=True)
        print("Создали сложный XML файл: complex_books.xml")

    @staticmethod
    def read_complex_xml():
        """Чтение сложного XML файла"""
        try:
            tree = ET.parse("complex_books.xml")
            root = tree.getroot()

            print("\n=== ЧТЕНИЕ СЛОЖНОГО XML ===")
            print(f"Версия: {root.get('версия')}")

            # Читаем информацию о магазине
            shop_info = root.find("информация_о_магазине")
            if shop_info is not None:
                name = shop_info.find("название").text
                print(f"Магазин: {name}")

            # Читаем книги
            catalog = root.find("каталог_книг")
            if catalog is not None:
                books = catalog.findall("книга")
                print(f"Найдено книг: {len(books)}")

                for book in books:
                    book_id = book.find("ид").text
                    title = book.find("название").text
                    price = book.find("цена").text
                    print(f"  - {title} (ID: {book_id}, цена: {price})")

            return root

        except FileNotFoundError:
            print("Файл complex_books.xml не найден!")
            return None
        except Exception as e:
            print(f"Ошибка чтения XML: {e}")
            return None


# Тестирование новых методов
if __name__ == "__main__":
    print("=== ТЕСТИРОВАНИЕ РАСШИРЕННЫХ ФАЙЛОВ ===")

    # Создаем файлы
    AdvancedFileWorker.create_complex_json()
    AdvancedFileWorker.create_complex_xml()

    # Читаем файлы
    AdvancedFileWorker.read_complex_json()
    AdvancedFileWorker.read_complex_xml()

    print("\nВсё готово! Проверьте файлы:")
    print(" - complex_books.json")
    print(" - complex_books.xml")