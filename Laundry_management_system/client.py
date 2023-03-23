from order import Order
import settings
from random import randint


class Client:
    def __init__(self, number_pone: str, name: str, email: str, address: str, password: str) -> None:
        self.subscriptions: dict = {"annual": False, "monthly": False, "daily": False}
        self.number_pone:str = number_pone
        self.name: str = name
        self.email = email
        self.address: str = address
        self.password: str = password
        self.orders: dict = {}

    def open_order(self):
        while True:
            NO_number = str(randint(1000000, 9999999))
            if NO_number not in 
        order = Order(self.email, str(randint(1000000, 9999999)))
        self.orders[order.NO] = order
        return order.NO


    def Order_pickup(self):
        pass