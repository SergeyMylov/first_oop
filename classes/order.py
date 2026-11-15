# classes/order.py
"""Класс, представляющий заказ."""

from .product import Product
from .discount import Discount


class Order:
    """
    Класс Order
    
        Этот класс представляет заказ в интернет-магазине.
    
        Атрибут класса total_orders_count:
            Счетчик всех созданных заказов. Это атрибут класса, а не экземпляра, поэтому он общий для всех объектов Order.
    
        Метод __init__:
            Конструктор принимает список товаров (products) и инициализирует объект Order.
            Увеличивает счетчик _total_orders на 1 каждый раз при создании нового заказа.
            Пример: order1 = Order([product1]) создаст заказ, содержащий один товар.
    
        Метод calculate_discounted_price:
            Статический метод, который принимает цену и скидку в процентах и возвращает цену после применения скидки.
            Пример: Order.calculate_discounted_price(1000, 10) вернет 900.0.
    
        Метод total_orders:
            Метод класса, который возвращает общее количество созданных заказов.
            Пример: Order.total_orders() вернет общее количество заказов.
    
        Метод total_price:
            Вычисляет общую стоимость всех товаров в заказе, суммируя их цены.
            Пример: order1.total_price() вернет 1000, если в заказе один товар с ценой 1000.
    
        Метод __str__:
            Возвращает строковое представление объекта заказа, включающее общую стоимость заказа.
            Пример: print(order1) выведет Order(total_price=1000)."""

    total_orders_count = 0  # Классовый атрибут для подсчёта общего количества заказов

    def __init__(self, products: list[Product] = None, discount: Discount = None):
        if products is None:
            products = []
        self.products = products
        self.discount = discount
        Order.total_orders_count += 1

    def calculate_total(self) -> float:
        """Расчёт итоговой суммы заказа с учётом скидки."""
        total = sum(product.price for product in self.products)
        if self.discount is not None:
            total = Discount.calculate_discounted_price(total, self.discount.discount_percent)
        return round(total, 2)

    def __str__(self) -> str:
        products_str = ", ".join([p.name for p in self.products]) if self.products else "no products"
        discount_str = f", discount: {self.discount.description} ({self.discount.discount_percent}%)" if self.discount else ""
        return f"Order(products=[{products_str}]{discount_str}, total={self.calculate_total():.2f})"

    @classmethod
    def get_total_orders_count(cls) -> int:
        """Метод класса для получения общего количества заказов."""
        return cls.total_orders_count

    @classmethod
    def get_total_all_orders_amount(cls, customers: list) -> float:
        """Метод класса для подсчёта общей суммы всех заказов для всех клиентов."""
        total_amount = 0.0
        for customer in customers:
            for order in customer.orders:
                total_amount += order.calculate_total()
        return round(total_amount, 2)
