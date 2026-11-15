# classes/customer.py
"""Класс, представляющий клиента."""

from .order import Order


class Customer:
    """
    Класс Customer
    
        Этот класс представляет клиента, 
        с атрибутами name (имя клиента) и 
        orders (список заказов клиента)."""
        
        

    def __init__(self, name: str):
        self.name = name
        self.orders: list[Order] = []

    def add_order(self, order: Order) -> None:
        """Добавление заказа к клиенту."""
        self.orders.append(order)

    def __str__(self) -> str:
        orders_str = ", ".join([str(order) for order in self.orders]) if self.orders else "no orders"
        return f"Customer(name='{self.name}', orders=[{orders_str}])"
