# main.py
"""
Интернет-магазин с системой скидок и учётом заказов - главный файл.
"""

from classes import Product, Customer, Order, Discount


def main():
    """Демонстрация работы системы интернет-магазина."""

    # Создание продуктов
    product1 = Product("Laptop", 50000.00)
    product2 = Product("Mouse", 1500.00)
    product3 = Product("Keyboard", 2500.00)
    product4 = Product("Monitor", 30000.00)
    product5 = Product("Headphones", 5000.00)

    # Создание клиентов
    customer1 = Customer("Алиса")
    customer2 = Customer("Михаил")
    customer3 = Customer("Сергей")

    # Создание скидок
    seasonal_discount = Discount("Сезонная скидка", 20)
    promo_discount = Discount("Скидка по промокоду SAVE15", 15)
    loyalty_discount = Discount("Скидка за лояльность", 10)

    # Создание заказов и добавление к клиентам
    order1 = Order([product1, product2, product3], seasonal_discount)
    customer1.add_order(order1)

    order2 = Order([product4, product5], promo_discount)
    customer2.add_order(order2)

    order3 = Order([product1, product5], loyalty_discount)
    customer3.add_order(order3)

    order4 = Order([product2, product3], None)  # Без скидки
    customer1.add_order(order4)

    order5 = Order([product4], seasonal_discount)
    customer2.add_order(order5)

    # Вывод информации о продуктах
    print("=" * 60)
    print("ПРОДУКТЫ:")
    print("=" * 60)
    for product in [product1, product2, product3, product4, product5]:
        print(f"  {product}")

    # Вывод информации о клиентах и заказах
    print()
    print("=" * 60)
    print("КЛИЕНТЫ И ИХ ЗАКАЗЫ:")
    print("=" * 60)
    for customer in [customer1, customer2, customer3]:
        print(f"\n{customer}")
        for order in customer.orders:
            print(f"    Заказ: {order}")
            print(f"    Итоговая сумма: {order.calculate_total():.2f}")

    # Подсчёт общего количества заказов
    print()
    print("=" * 60)
    print("СТАТИСТИКА:")
    print("=" * 60)
    total_orders = Order.get_total_orders_count()
    print(f"Общее количество заказов: {total_orders}")

    # Подсчёт общей суммы всех заказов для всех клиентов
    all_customers = [customer1, customer2, customer3]
    total_amount = Order.get_total_all_orders_amount(all_customers)
    print(f"Общая сумма всех заказов: {total_amount:.2f}")

    # Демонстрация статических методов Discount
    print()
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ СТАТИЧЕСКИХ МЕТОДОВ DISCOUNT:")
    print("=" * 60)
    original_price = 10000.0
    print(f"  Исходная цена: {original_price:.2f}")
    print(f"  Сезонная скидка (20%): {Discount.apply_seasonal_discount(original_price):.2f}")
    print(f"  Скидка по промокоду (15%): {Discount.apply_promo_code_discount(original_price):.2f}")
    print(f"  Скидка за лояльность (10%): {Discount.apply_loyalty_discount(original_price):.2f}")
    print(f"  Расчёт вручную (25%): {Discount.calculate_discounted_price(original_price, 25):.2f}")


if __name__ == "__main__":
    main()
