from itertools import product


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def file_name(self):
        return self.__file_name

    def get_products(self):
        with open(self.__file_name, mode='r', encoding='utf8') as file:
            file_products = file.read()
        return file_products

    def add(self, *products):
        with open(self.__file_name, mode='r', encoding='utf8') as file:
            line = True
            for line in file:
                self.get_products()
                if str(products) in line:
                    print(f'Продукт {products} уже есть в магазине')
                    break
                else:
                    file.write(f'{products}\n')



shop = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

shop.add(p1, p2, p3)

print(shop.get_products())