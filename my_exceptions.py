# Мои исключения для лабы

class MyBaseError(Exception):
    """Базовая ошибка для моей программы"""
    pass

class MoneyError(MyBaseError):
    """Ошибка с деньгами"""
    def __init__(self, user_name, need_money, has_money):
        self.user = user_name
        self.need = need_money
        self.has = has_money
        message = f"У {user_name} мало денег! Нужно: {need_money}, есть: {has_money}"
        super().__init__(message)

class FormatError(MyBaseError):
    """Ошибка формата файла"""
    def __init__(self, bad_format, good_formats):
        self.bad = bad_format
        self.good = good_formats
        message = f"Формат {bad_format} не подходит! Можно: {', '.join(good_formats)}"
        super().__init__(message)

class EmptyCartError(MyBaseError):
    """Ошибка пустой корзины"""
    def __init__(self):
        super().__init__("Нельзя оформить пустую корзину!")