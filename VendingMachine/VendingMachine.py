class Product:
    def __init__(self, name: str, price: float, quantity: str):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product is {self.name} with (${self.price:.2f}) and qty {self.quantity}"

class VendingMachine:
    def __init__(self):
        self.products = {}
        self.transaction_money = 0.0

    
    def add_product(self, code: str, product:Product):
        if code in self.products:
            print("product already present")
            return 
        else:
            self.products[code] = product

    def insert_money(self, money: float):
        if money <= 0:
            print("insert valid money")
            return
        else:
            self.transaction_money += money

    def select_product(self, code:str):
        if code not in self.products:
            print("product not present")
            return
        product = self.products[code]
        if product.quantity <= 0:
            print("Product is out of stock")
            return
        if self.transaction_money < product.price:
            print("insufficient funds, please insert more money")
            return
        product.quantity -= 1
        print("Dispensing product: ", product)
        change = self.transaction_money - product.price
        if change >= 0:
            print(f"returning change ${change:.2f}")
        self.transaction_money = 0.0
        

    def cancel_transaction(self):
        if self.transaction_money > 0:
            print(f"Transaction cancelled, returning {self.transaction_money:.2f}")
            return
        else:
            print(f"No transaction to cancel")


    def display_products(self):
        for code, product in self.Product.items():
            print(f"{code} - {product}")


def main():
    machine = VendingMachine()
    product1 = Product("Snack bar",2.50,10)
    product2 = Product("Chocolate",1.50,7)
    product3 = Product("Coke",3.50,5)
    product4 = Product("Lays",2.50,13)
    machine.add_product("A1",product1)
    machine.add_product("B3",product2)
    machine.add_product("C1",product3)
    machine.add_product("A2",product4)
    machine.add_product("A2",product4)

    machine.display_products()
    machine.insert_money(3)
    machine.select_product("A1")
    machine.insert_money(1)
    machine.select_product("C1")
    machine.insert_money(5)
    machine.cancel_transaction()

    machine.display_products()

if __name__ == "main":
    main()