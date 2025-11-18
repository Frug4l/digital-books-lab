"""Модуль для работы с файлами JSON и XML."""

import json
import xml.etree.ElementTree as ET


class AdvancedFileWorker:
    """Класс для работы с файлами JSON и XML."""

    @staticmethod
    def create_complex_json():
        """Создание сложного JSON файла."""
        data = {
            "book_store": {
                "name": "Интернет-магазин цифровых книг",
                "version": "1.0",
                "creation_date": "2024",
                "books": [
                    {
                        "book_id": 101,
                        "title": "Война и мир",
                        "author": {
                            "author_id": 1,
                            "name": "Толстой Л.Н.",
                            "bio": "Великий русский писатель"
                        },
                        "price": 299.99,
                        "currency": "руб",
                        "format": "PDF",
                        "size_mb": 15,
                        "rating": 4.8
                    },
                    {
                        "book_id": 102,
                        "title": "Евгений Онегин",
                        "author": {
                            "author_id": 2,
                            "name": "Пушкин А.С.",
                            "bio": "Великий русский поэт"
                        },
                        "price": 199.5,
                        "currency": "руб",
                        "format": "EPUB",
                        "size_mb": 3,
                        "rating": 4.9
                    }
                ],
                "customers": [
                    {
                        "customer_id": 1,
                        "name": "Иванов Иван",
                        "email": "ivanov@mail.ru",
                        "registration_date": "2024-01-15"
                    }
                ]
            }
        }

        try:
            with open("complex_books.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print("Создали сложный JSON файл: complex_books.json")
        except (IOError, TypeError) as error:
            print(f"Ошибка при создании JSON: {error}")

    @staticmethod
    def read_complex_json():
        """Чтение сложного JSON файла."""
        try:
            with open("complex_books.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            print("\n=== ЧТЕНИЕ СЛОЖНОГО JSON ===")
            shop_info = data["book_store"]
            print(f"Магазин: {shop_info['name']}")
            print(f"Книг в каталоге: {len(shop_info['books'])}")

            for book in shop_info["books"]:
                print(f"  - {book['title']} ({book['price']} {book['currency']})")

            return data

        except FileNotFoundError:
            print("Файл complex_books.json не найден!")
            return None
        except (json.JSONDecodeError, KeyError) as error:
            print(f"Ошибка чтения JSON: {error}")
            return None

    @staticmethod
    def create_complex_xml():
        """Создание сложного XML файла."""
        root = ET.Element("digital_library")
        root.set("version", "1.0")
        root.set("creation_date", "2024")

        shop_info = ET.SubElement(root, "shop_info")
        ET.SubElement(shop_info, "name").text = "Магазин цифровых книг"
        ET.SubElement(shop_info, "website").text = "www.books.ru"
        ET.SubElement(shop_info, "phone").text = "8-800-123-45-67"

        authors = ET.SubElement(root, "authors")
        author1 = ET.SubElement(authors, "author")
        ET.SubElement(author1, "id").text = "1"
        ET.SubElement(author1, "name").text = "Толстой Л.Н."
        ET.SubElement(author1, "country").text = "Россия"

        author2 = ET.SubElement(authors, "author")
        ET.SubElement(author2, "id").text = "2"
        ET.SubElement(author2, "name").text = "Пушкин А.С."
        ET.SubElement(author2, "country").text = "Россия"

        catalog = ET.SubElement(root, "book_catalog")
        book1 = ET.SubElement(catalog, "book")
        book1.set("category", "classic")
        ET.SubElement(book1, "id").text = "101"
        ET.SubElement(book1, "title").text = "Война и мир"
        ET.SubElement(book1, "author_id").text = "1"
        ET.SubElement(book1, "price").text = "299.99"
        ET.SubElement(book1, "rating").text = "4.8"

        book2 = ET.SubElement(catalog, "book")
        book2.set("category", "poetry")
        ET.SubElement(book2, "id").text = "102"
        ET.SubElement(book2, "title").text = "Евгений Онегин"
        ET.SubElement(book2, "author_id").text = "2"
        ET.SubElement(book2, "price").text = "199.50"
        ET.SubElement(book2, "rating").text = "4.9"

        tree = ET.ElementTree(root)
        tree.write("complex_books.xml", encoding="utf-8", xml_declaration=True)
        print("Создали сложный XML файл: complex_books.xml")

    @staticmethod
    def read_complex_xml():
        """Чтение сложного XML файла."""
        try:
            tree = ET.parse("complex_books.xml")
            root = tree.getroot()

            print("\n=== ЧТЕНИЕ СЛОЖНОГО XML ===")
            print(f"Версия: {root.get('version')}")

            shop_info = root.find("shop_info")
            if shop_info is not None:
                name = shop_info.find("name").text
                print(f"Магазин: {name}")

            catalog = root.find("book_catalog")
            if catalog is not None:
                books = catalog.findall("book")
                print(f"Найдено книг: {len(books)}")

                for book in books:
                    book_id = book.find("id").text
                    title = book.find("title").text
                    price = book.find("price").text
                    print(f"  - {title} (ID: {book_id}, цена: {price})")

            return root

        except FileNotFoundError:
            print("Файл complex_books.xml не найден!")
            return None
        except ET.ParseError as error:
            print(f"Ошибка чтения XML: {error}")
            return None
