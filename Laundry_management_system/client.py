from order import Order
import settings
from random import randint
from mysql_database import MysqlDatabase


class Client:
    def __init__(self, number_pone: str, name: str, family: str, city: str, street: str, house_number: int, email: str, password: str) -> None:
        self.subscriptions: dict = {"annual": False, "monthly": False, "daily": False}
        self.number_pone:str = number_pone
        self.name: str = name
        self.family = family
        self.city = city
        self.street = street
        self.house_number = house_number
        self.email = email
        self.password: str = password
        self.orders: dict = {}
        self.insert_to_sql()

    def insert_to_sql(self):
        if not MysqlDatabase.check_client_existence(self.email):
            MysqlDatabase.add_client(self.name, self.family, self.city, self.street, self.house_number, self.number_pone,self.email, self.password)
        

    def open_order(self):
        new_order = Order(self.email)
        self.orders[new_order.ID] = new_order


    def Order_pickup(self):
        pass



# noach = Client("0527194022", "noah", "tzitrenboim", "bet shemesh", "miryam", 12, "t0527184022@gmail.com", "2345")
# noach.open_order()
# MysqlDatabase.print_by_pd("orders")
# MysqlDatabase.print_by_pd("clients")