class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return print(f'{self.name}, {self.weight}, {self.category}')


class Shop(Product):

    __file_name = 'products.txt'
    def __init__(self, Shop):
        self.Shop = Shop()
    def get_products(self, __file_name):
        file = open(__file_name, 'r')
        file.close()
        return __file_name

    def add(self, *products):
        file = open(self.__file_name, 'a')
        if products in self.__file_name:
            print(f'\nПродукт {self.name} уже есть в магазине')
        else:
            file.write(products)
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())