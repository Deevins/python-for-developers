from pydantic import BaseModel, Field, validator
from typing import Dict, List
from uuid import uuid4, UUID


class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=3, description="Название товара")
    price: float = Field(..., gt=0, description="Цена товара должна быть больше 0")
    stock: int = Field(..., ge=0, description="Количество товара на складе не может быть отрицательным")

    def update_stock(self, quantity: int):
        if self.stock + quantity < 0:
            raise ValueError("Недостаточно товара на складе для выполнения операции.")
        self.stock += quantity

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self):
        return f"{self.name} (ID: {self.id}, Цена: {self.price}, На складе: {self.stock})"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)


class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    products: Dict[Product, int] = Field(default_factory=dict)

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError("Недостаточно товара на складе для добавления в заказ.")
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity
        product.update_stock(-quantity)

    def remove_product(self, product: Product, quantity: int):
        if product not in self.products:
            raise ValueError("Товар не найден в заказе.")
        if self.products[product] < quantity:
            raise ValueError("Нельзя удалить больше товара, чем добавлено в заказ.")

        self.products[product] -= quantity
        product.update_stock(quantity)
        if self.products[product] == 0:
            del self.products[product]

    def calculate_total(self) -> float:
        return sum(product.price * quantity for product, quantity in self.products.items())

    def return_product(self, product: Product, quantity: int):
        if product not in self.products:
            raise ValueError("Товар не найден в заказе.")
        if self.products[product] < quantity:
            raise ValueError("Нельзя вернуть больше товара, чем добавлено в заказ.")

        self.products[product] -= quantity
        product.update_stock(quantity)
        if self.products[product] == 0:
            del self.products[product]

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self):
        items = ", ".join(f"{product.name}: {quantity}" for product, quantity in self.products.items())
        return f"Заказ(ID: {self.id}, Продукты: {items})"


class Store(BaseModel):
    products: List[Product] = Field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product)


    def create_order(self) -> Order:
        return Order()

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self):
        return f"Магазин({len(self.products)} товаров)"