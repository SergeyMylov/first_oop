# classes/discount.py
"""Класс для применения скидок."""


class Discount:
    """Этот класс для применения скидок, 
        с атрибутами description (описание скидки) и 
        discount_percent (процент скидки).
    ."""

    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    def __str__(self) -> str:
        return f"Discount(description='{self.description}', discount_percent={self.discount_percent:.1f}%)"

    @staticmethod
    def calculate_discounted_price(original_price: float, discount_percent: float) -> float:
        """Статический метод для расчёта цены со скидкой."""
        discounted_price = original_price * (1 - discount_percent / 100)
        return round(discounted_price, 2)

    @staticmethod
    def apply_seasonal_discount(price: float) -> float:
        """Применение сезонной скидки (20%)."""
        return Discount.calculate_discounted_price(price, 20)

    @staticmethod
    def apply_promo_code_discount(price: float) -> float:
        """Применение скидки по промокоду (15%)."""
        return Discount.calculate_discounted_price(price, 15)

    @staticmethod
    def apply_loyalty_discount(price: float) -> float:
        """Применение скидки за лояльность (10%)."""
        return Discount.calculate_discounted_price(price, 10)
