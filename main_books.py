
from datetime import datetime
import random


class MyBaseError(Exception):
    """Базовая ошибка для программы."""

    pass


class MoneyError(MyBaseError):
    """Ошибка с деньгами."""

    def __init__(self, user_name, need_money, has_money):
        self.user = user_name
        self.need = need_money
        self.has = has_money
        message = f"У {user_name} мало денег! Нужно: {need_money}, есть: {has_money}"
        super().__init__(message)


class FormatError(MyBaseError):
    """Ошибка формата файла."""

    def __init__(self, bad_format, good_formats):
        self.bad = bad_format
        self.good = good_formats
        message = f"Формат {bad_format} не подходит! Можно: {', '.join(good_formats)}"
        super().__init__(message)


class EmptyCartError(MyBaseError):
    """Ошибка пустой корзины."""

    def __init__(self):
        super().__init__("Нельзя оформить пустую корзину!")


class Author:
    """Класс автора книги."""

    def __init__(self, author_id, name, bio=""):
        self.id = author_id
        self.name = name
        self.bio = bio

    def show_info(self):
        """Показать информацию об авторе."""
        return f"Автор: {self.name} (ID: {self.id})"

    def __str__(self):
        return self.name


class DigitalBook:
    """Класс цифровой книги."""

    VALID_FORMATS = ['PDF', 'EPUB', 'FB2', 'MOBI']

    def __init__(self, book_id, title, author, price, book_format, size):
        self.id = book_id
        self.title = title
        self.author = author
        self.price = price

        # Проверка формата с использованием кастомного исключения
        if book_format.upper() not in self.VALID_FORMATS:
            raise FormatError(book_format, self.VALID_FORMATS)

        self.format = book_format.upper()
        self.size = size

    def get_book_info(self):
        """Получить информацию о книге."""
        info = f"'{self.title}' - {self.author.name}"
        info += f" | {self.format} | {self.size}MB"
        info += f" | Цена: {self.price} руб."
        return info

    def __str__(self):
        return self.title


class Customer:
    """Класс покупателя."""

    def __init__(self, customer_id, name, email, balance=0.0):
        self.id = customer_id
        self.name = name
        self.email = email
        self.balance = balance
        self.cart = ShoppingCart(self)

    def __str__(self):
        return f"Покупатель: {self.name}"


class ShoppingCart:
    """Класс корзины покупок."""

    def __init__(self, customer):
        self.id = int(str(customer.id) + str(random.randint(1000, 9999)))
        self.owner = customer
        self.book_list = []

    def add_book(self, book):
        """Добавить книгу в корзину."""
        self.book_list.append(book)
        print(f"Добавили '{book.title}' в корзину")

    def remove_book(self, book):
        """Удалить книгу из корзины."""
        if book in self.book_list:
            self.book_list.remove(book)
            print(f"Удалили '{book.title}' из корзины")
        else:
            print("Этой книги нет в корзине!")

    def get_total_price(self):
        """Посчитать общую стоимость."""
        total = 0.0
        for book in self.book_list:
            total += book.price
        return round(total, 2)

    def make_order(self):
        """Оформить заказ."""
        if not self.book_list:
            raise EmptyCartError()

        total = self.get_total_price()

        # Проверка баланса
        if self.owner.balance < total:
            raise MoneyError(self.owner.name, total, self.owner.balance)

        new_order = Order(
            order_id=len(self.book_list) * 1000 + random.randint(100, 999),
            customer=self.owner,
            books=self.book_list.copy(),
            total=total
        )

        # Списание средств
        self.owner.balance -= total

        # Очищаем корзину после заказа
        self.book_list.clear()
        print("Заказ создан успешно!")
        return new_order

    def __str__(self):
        return f"Корзина {self.owner.name} ({len(self.book_list)} книг)"


class Order:
    """Класс заказа."""

    def __init__(self, order_id, customer, books, total):
        self.id = order_id
        self.customer = customer
        self.books = books
        self.total = total
        self.date = datetime.now()

    def create_receipt(self):
        """Сгенерировать чек."""
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
