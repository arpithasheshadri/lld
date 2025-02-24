# Customer - view the menu, place an order, pay
# Menu - food, name,category,price and availability status
# Menu item  
# Order - mul items, ord -> table num, status -> Pending,Preparing,Ready and Served
# OrderItem - 
# Payment - cash, credit or digital wallets, genBill()
# Staff - Waiter, Cashier, Chef
# 
# Table ?

from enum import Enum

class OrderStatus(Enum):
    PENDING = "Pending"
    PREPARING = "Preparing"
    READY = "Ready"
    SERVED = "Served"

class PaymentMethod(Enum):
    CASH = "Cash"
    CREDIT = "Credit"
    DIGITAL_WALLET = "DigitalWallet"

class MenuItem:
    def __init__(self, name:str, category:str, price:float, availability_status: bool = True):
        self.name = name
        self.category = category
        self.price = price
        self.availability_status = availability_status


    def __str__(self):
        print(f"Menu Item: {self.name} - {self.category} - ${self.price:.2f}")

class Menu:
    def __init__(self):
        self.menu = []

    def add_menu_item(self, item: MenuItem):
        self.menu.append(item)
    
    def display_menu(self):
        for i in self.menu:
            print(f"{i.name} - {i.category} - {i.price} - {i.availability_status}")

class Customer:
    def __init__(self, name:str, contact:str):
        self.name =  name
        self.contact = contact

class OrderItem:
    def __init__(self, menu_item:MenuItem, quantity: int):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_total_price(self):
        return self.menu_item.price * self.quantity

class Order:
    def __init__(self,customer: Customer,table_no: int = None):
        self.customer = customer
        self.table_no = table_no
        self.order = []
        self.status = OrderStatus.PENDING

    def add_order_item(self, item: MenuItem, quantity: int):
        if not item.availability_status:
            print(f"Sorry, {item.name} is not available.")
            return
        self.order.append(OrderItem(item, quantity))

    def update_status(self, order_status: OrderStatus):
        self.status = order_status

    def get_bill(self):
        return sum(item.get_total_price() for item in self.order)

    def __str__(self):
        return f"Order for {self.customer.name} | Table {self.table_no if self.table_no else 'Takeaway'} | Status: {self.status.value}"


class Table:
    def __init__(self, table_num: int, capacity: int):
        self.table_num = table_num
        self.capacity = capacity
        self.occupied = False

    def occupy(self):
        if self.occupied:
            print(f"Table {self.table_number} is already occupied.")
        else:
            self.occupied = True 

    def vacate(self):
        self.occupied = False
    

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return  f"{self.role}:{self.name}"
        

class Waiter(Staff):
    def __init__(self, name):
        super().__init__(name, "Waiter")

    def take_order(self,customer: Customer, table_no: int):
        print(f"Waiter has taken order for {table_no} ")
        return Order(customer,table_no)
    

class Cashier(Staff):
    def __init__(self, name):
        super().__init__(name, "Cashier")

    def process_payment(self,order: Order, payment_method: PaymentMethod):
        total = order.get_bill()
        print(f"{self.name} processed ${total:.2f} payment using {payment_method.value}.")
        order.update_status(OrderStatus.SERVED)


class Chef(Staff):
    def __init__(self, name):
        super().__init__(name, "Chef")

    def prepare_order(self, order: Order):
        print(f"{self.name} is preparing the order for {order.customer.name}")
        order.update_status(OrderStatus.PREPARING)

class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.tables = [Table(i,4) for i in range(1,6)]
        self.orders = []

    def add_menu_item(self, item:MenuItem):
        self.menu.add_menu_item(item)

    def place_order(self, order: Order):
        self.orders.append(order)

    def show_orders(self):
        print("\nCurrent Orders:")
        for order in self.orders:
            print(order)

def main():
    restaurant = Restaurant()

    # Add menu items
    restaurant.add_menu_item(MenuItem("Pizza", "Main Course", 10.99))
    restaurant.add_menu_item(MenuItem("Burger", "Main Course", 5.99))
    restaurant.add_menu_item(MenuItem("Soda", "Beverage", 1.99))

    # Display the menu
    restaurant.menu.display_menu()

    # Create staff
    waiter = Waiter("John")
    chef = Chef("Alice")
    cashier = Cashier("Bob")

    # Create customer and place order
    customer1 = Customer("Alice", "123-456-7890")
    order1 = waiter.take_order(customer1, 1)
    order1.add_order_item(restaurant.menu.menu[0], 2)  # Pizza x2
    restaurant.place_order(order1)

    # Show orders
    restaurant.show_orders()

    # Chef prepares the order
    chef.prepare_order(order1)

    # Customer pays the bill
    cashier.process_payment(order1, PaymentMethod.CREDIT)

    # Show orders after completion
    restaurant.show_orders()

if __name__ == "__main__":
    main()