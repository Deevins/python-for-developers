import unittest
from uuid import UUID
from models import Store, Product


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.product1 = Product(name="Ноутбук", price=30000, stock=10)
        self.product2 = Product(name="Наушники", price=3000, stock=20)
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)

    def test_product_creation_with_uuid(self):
        self.assertIsInstance(self.product1.id, UUID)
        self.assertIsInstance(self.product2.id, UUID)

    def test_order_creation_with_uuid(self):
        order = self.store.create_order()
        self.assertIsInstance(order.id, UUID)

    def test_add_product_to_order(self):
        order = self.store.create_order()
        order.add_product(self.product1, 2)
        self.assertEqual(order.products[self.product1], 2)
        self.assertEqual(self.product1.stock, 8)

    def test_remove_product_from_order(self):
        order = self.store.create_order()
        order.add_product(self.product2, 5)
        order.remove_product(self.product2, 3)
        self.assertEqual(order.products[self.product2], 2)
        self.assertEqual(self.product2.stock, 18)

    def test_return_product_to_store(self):
        order = self.store.create_order()
        order.add_product(self.product1, 4)
        order.return_product(self.product1, 2)
        self.assertEqual(order.products[self.product1], 2)
        self.assertEqual(self.product1.stock, 8)

    def test_calculate_order_total(self):
        order = self.store.create_order()
        order.add_product(self.product1, 1)
        order.add_product(self.product2, 3)
        total = order.calculate_total()
        self.assertEqual(total, 30000 + 3 * 3000)

    def test_list_products_in_store(self):
        self.assertIn(self.product1, self.store.products)
        self.assertIn(self.product2, self.store.products)

    def test_stock_update_error(self):
        with self.assertRaises(ValueError):
            self.product1.update_stock(-15)

    def test_add_product_insufficient_stock_error(self):
        order = self.store.create_order()
        with self.assertRaises(ValueError):
            order.add_product(self.product1, 11)

    def test_remove_product_not_in_order_error(self):
        order = self.store.create_order()
        with self.assertRaises(ValueError):
            order.remove_product(self.product1, 1)

    def test_return_product_not_in_order_error(self):
        order = self.store.create_order()
        with self.assertRaises(ValueError):
            order.return_product(self.product2, 1)


if __name__ == '__main__':
    unittest.main()
