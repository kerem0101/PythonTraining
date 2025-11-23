from item import Item 

class Phone(Item):
    def __init__(self, name, price, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"broken_phones: {broken_phones} cannot be negative" 

        self.broken_phones = broken_phones

phone1 = Phone("myPhone", 46000, 6, 1)

for item in Item.all:
    print(f"name: {item.name}, price: {item.price}, quantity: {item.quantity}")



