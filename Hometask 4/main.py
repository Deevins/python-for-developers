from models import Store, Product




# Основная программа
def main() -> None:
    store = Store()

    # Создаем товары
    product1 = Product(name="Ноутбук", price=10000, stock=5)
    product2 = Product(name="Смартфон", price=500, stock=10)

    # Добавляем товары в магазин
    store.add_product(product1)
    store.add_product(product2)

    # Список всех товаров
    store.list_products()

    # Создаем заказ
    order = store.create_order()

    # Добавляем товары в заказ
    order.add_product(product1, 2)
    order.add_product(product2, 3)

    # Выводим общую стоимость заказа
    total = order.calculate_total()
    print(f"Общая стоимость заказа: {total}")

    # Проверяем остатки на складе после заказа
    store.list_products()


if __name__ == "__main__":
    main()
