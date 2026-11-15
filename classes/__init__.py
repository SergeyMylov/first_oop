# classes/__init__.py
"""Пакет классов для интернет-магазина."""

from .product import Product
from .customer import Customer
from .order import Order
from .discount import Discount

__all__ = ['Product', 'Customer', 'Order', 'Discount']
