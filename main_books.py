# -*- coding: utf-8 -*-
# Лаба по ООП - продажа цифровых книг
# Сделал: [Твое имя], группа [Твоя группа]

from datetime import datetime


# Класс для автора книги
class Author:
    def __init__(self, id_author, name_author, bio_text=""):
        self.id = id_author
        self.name = name_author
        self.bio = bio_text

    # Вывод информации об авторе
    def show_info(self):
        return f"Автор: {self.name} (ID: {self.id})"

    def __str__(self):
        return self.name


# Класс для цифровой книги
class DigitalBook:
    # Список разрешенных форматов
    valid_formats = ['PDF', 'EPUB', 'FB2', 'MOBI']

    def __init__(self, id_book, title_book, author_obj, price_book, format_book, size_book):
        self.id = id_book
        self.title = title_book
        self.author = author_obj
        self.price = price_book

        # Проверка формата
        if format_book.upper() not in self.valid_formats:
            raise ValueError(f"Формат {format_book} не поддерживается!")

        self.format = format_book.upper()
        self.size = size_book  # в мегабайтах

    # Получить информацию о книге
    def get_book_info(self):
        info = f"'{self.title}' - {self.author.name}"
        info += f" | {self.format} | {self.size}MB"
        info += f" | Цена: {self.price} руб."
        return info

    def __str__(self):
        return self.title


# Класс покупателя
class Customer:
    def __init__(self, id_customer, name_customer, email_customer):
        self.id = id_customer
        self.name = name_customer
        self.email = email_customer
        # Создаем корзину для этого покупателя
        self.cart = ShoppingCart(self)

    def __str__(self):
        return f"Покупатель: {self.name}"


# Класс корзины покупок
class ShoppingCart:
    def __init__(self, customer_obj):
        self.id = hash(str(customer_obj.id) + str(datetime.now()))
        self.owner = customer_obj
        self.book_list = []  # список книг в корзине

    # Добавить книгу в корзину
    def add_book(self, book_obj):
        self.book_list.append(book_obj)
        print(f"Добавили '{book_obj.title}' в корзину")

    # Удалить книгу из корзины
    def remove_book(self, book_obj):
        if book_obj in self.book_list:
            self.book_list.remove(book_obj)
            print(f"Удалили '{book_obj.title}' из корзины")
        else:
            print("Этой книги нет в корзине!")

    # Посчитать общую стоимость
    def get_total_price(self):
        total = 0.0
        for book in self.book_list:
            total += book.price
        return round(total, 2)

    # Оформить заказ
    def make_order(self):
        if len(self.book_list) == 0:
            print("Ошибка: корзина пустая!")
            return None

        total = self.get_total_price()
        new_order = Order(
            id_order=len(self.book_list) * 1000 + hash(str(datetime.now())) % 1000,
            customer_obj=self.owner,
            books_list=self.book_list.copy(),
            total_sum=total
        )

        # Очищаем корзину после заказа
        self.book_list.clear()
        print("Заказ создан успешно!")
        return new_order

    def __str__(self):
        return f"Корзина {self.owner.name} ({len(self.book_list)} книг)"


# Класс заказа
class Order:
    def __init__(self, id_order, customer_obj, books_list, total_sum):
        self.id = id_order
        self.customer = customer_obj
        self.books = books_list
        self.total = total_sum
        self.date = datetime.now()

    # Сгенерировать чек
    def create_receipt(self):
        receipt = "=" * 40 + "\n"
        receipt += "ЧЕК ЗАКАЗА\n"
        receipt += "=" * 40 + "\n"
        receipt += f"Заказ №: {self.id}\n"
        receipt += f"Клиент: {self.customer.name}\n"
        receipt += f"Дата: {self.date.strftime('%d.%m.%Y %H:%M')}\n"
        receipt += "-" * 40 + "\n"
        receipt += "Книги:\n"

        for i, book in enumerate(self.books, 1):
            receipt += f"{i}. {book.title} - {book.price} руб.\n"

        receipt += "-" * 40 + "\n"
        receipt += f"ИТОГО: {self.total} руб.\n"
        receipt += "=" * 40
        return receipt

    def __str__(self):
        return f"Заказ №{self.id} на {self.total} руб."


# Демонстрация работы
if __name__ == "__main__":
    print("=== ТЕСТИРОВАНИЕ СИСТЕМЫ ===\n")

    try:
        # Создаем авторов
        author1 = Author(1, "Толстой Л.Н.", "Русский классик")
        author2 = Author(2, "Пушкин А.С.", "Великий поэт")
        author3 = Author(3, "Достоевский Ф.М.")

        print("Создали авторов:")
        print(author1.show_info())
        print(author2.show_info())
        print()

        # Создаем книги
        book1 = DigitalBook(101, "Война и мир", author1, 299.99, "PDF", 15)
        book2 = DigitalBook(102, "Евгений Онегин", author2, 199.50, "EPUB", 3)
        book3 = DigitalBook(103, "Преступление и наказание", author3, 249.99, "FB2", 8)

        print("Создали книги:")
        print(book1.get_book_info())
        print(book2.get_book_info())
        print(book3.get_book_info())
        print()

        # Создаем покупателя
        customer = Customer(1, "Иванов Иван", "ivanov@mail.ru")
        print(f"Создали покупателя: {customer}")
        print()

        # Работа с корзиной
        print("--- Работа с корзиной ---")
        customer.cart.add_book(book1)
        customer.cart.add_book(book2)
        customer.cart.add_book(book3)

        print(f"В корзине: {len(customer.cart.book_list)} книг")
        print(f"Общая стоимость: {customer.cart.get_total_price()} руб.")
        print()

        # Пробуем оформить заказ
        print("--- Оформление заказа ---")
        order = customer.cart.make_order()
        if order:
            print(order.create_receipt())

        # Проверяем что корзина пустая
        print(f"Книг в корзине после заказа: {len(customer.cart.book_list)}")

    except Exception as e:
        print(f"Ошибка: {e}")