
from pprint import pprint
import os

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

    def __eq__(self, other):
        return (self.name == other.name and
                self.weight == other.weight and
                self.category == other.category)


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
            self.products_in_shop = []
            file = open(self.__file_name, 'r')
            for line in file:
                if line!='':
                    name, weight, category = line.strip().split(', ')
                    self.products_in_shop.append(Product(name, float(weight), category))
            file.close()


    def add(self, *products):
        self.get_products()
        for product in products:
            if product not in self.products_in_shop:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato',  50.5, 'Vegitables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
s1.add(p1, p2, p3)
s1.get_products()
print(p1)
print(p2)
print(p3)