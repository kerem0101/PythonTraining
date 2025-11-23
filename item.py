import csv

class Item:
    
    pay_rate = 0.8
    all = []

    def __init__(self, name:str, price:float, quantity=0):
        assert price >= 0, f"price: {price} cannot be negative"
        assert quantity >= 0, f"quantity: {quantity} cannot be negative"
        
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_dicount(self):
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("name is too long!")
        else: 
            self.__name = value

    @classmethod
    def instantiate_csv_file(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')), 
            )

    @staticmethod
    def is_instance(num):
        if isinstance(num, int):
            return True
        else:
            return False


#Item.instantiate_csv_file()

item1 = Item("laptop", 50000, 6)

item1.name = "laptops"

for item in Item.all:
    print(f"name: {item.name}, price: {item.price}, quantity: {item.quantity}")


#print(Item.is_instance(5))

