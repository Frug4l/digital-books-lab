from datetime import datetime

# Класс для автора книги
class Author:
    def __init__(self, id_author, name_author, bio_text=""):
        self.id = id_author
        self.name = name_author
        self.bio = bio_text

    # Вывод информации об авторе
    def show_info(self):
        return "Автор: {0} (ID: {1})".format(self.name, self.id)

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
            raise ValueError("Формат {0} не поддерживается!".format(format_book))

        self.format = format_book.upper()
        self.size = size_book  # в мегабайтах

    # Получить информацию о книге
    def get_book_info(self):
        info = "'{0}' - {1}".format(self.title, self.author.name)
        info += " | {0} | {1}MB".format(self.format, self.size)
        info += " | Цена: {0} руб.".format(self.price)
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
        return "Покупатель: {0}".format(self.name)

# Класс корзины покупок
class ShoppingCart:
    def __init__(self, customer_obj):
        self.id = hash(str(customer_obj.id) + str(datetime.now()))
        self.owner = customer_obj
        self.book_list = []  # список книг в корзине

    # Добавить книгу в корзину
    def add_book(self, book_obj):
        self.book_list.append(book_obj)
        print("Добавили '{0}' в корзину".format(book_obj.title))

    # Удалить книгу из корзины
    def remove_book(self, book_obj):
        if book_obj in self.book_list:
            self.book_list.remove(book_obj)
            print("Удалили '{0}' из корзины".format(book_obj.title))
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
            books_list=self.book_list[:],
            total_sum=total
        )

        # Очищаем корзину после заказа
        self.book_list = []
        print("Заказ создан успешно!")
        return new_order

    def __str__(self):
        return "Корзина {0} ({1} книг)".format(self.owner.name, len(self.book_list))

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
        receipt += "Заказ №: {0}\n".format(self.id)
        receipt += "Клиент: {0}\n".format(self.customer.name)
        receipt += "Дата: {0}\n".format(self.date.strftime('%d.%m.%Y %H:%M'))
        receipt += "-" * 40 + "\n"
        receipt += "Книги:\n"

        for i, book in enumerate(self.books, 1):
            receipt += "{0}. {1} - {2} руб.\n".format(i, book.title, book.price)

        receipt += "-" * 40 + "\n"
        receipt += "ИТОГО: {0} руб.\n".format(self.total)
        receipt += "=" * 40
        return receipt

    def __str__(self):
        return "Заказ №{0} на {1} руб.".format(self.id, self.total)

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
        print("Создали покупателя: {0}".format(customer))
        print()

        # Работа с корзиной
        print("--- Работа с корзиной ---")
        customer.cart.add_book(book1)
        customer.cart.add_book(book2)
        customer.cart.add_book(book3)

        print("В корзине: {0} книг".format(len(customer.cart.book_list)))
        print("Общая стоимость: {0} руб.".format(customer.cart.get_total_price()))
        print()

        # Пробуем оформить заказ
        print("--- Оформление заказа ---")
        order = customer.cart.make_order()
        if order:
            print(order.create_receipt())

        # Проверяем что корзина пустая
        print("Книг в корзине после заказа: {0}".format(len(customer.cart.book_list)))

    except Exception as e:
        print("Ошибка: {0}".format(e))
