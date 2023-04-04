from typing import Type
import settings
from mysql_database import MysqlDatabase

class Order:
    start_ID = MysqlDatabase.check_start_ID_orders()
    def __init__(self, email_client: str) -> None:
        self.email_client = email_client 
        self.items:dict = {}
        self.ID = Order.start_ID
        Order.start_ID += 1
        self.amount = self.calculate()
        self.insert_to_sql()

    def calculate(self) -> int:
        sum_order: int = sum(settings.PRISE_LIST[item] * self.items[item] for item in self.items)
        return (max(settings.MIN_ORDER, sum_order))
    
    def add_item(self, item: str) -> bool:
        if item not in settings.PRISE_LIST:
            return False
        self.items[item] += 1
        return True
            
    def insert_to_sql(self):
        MysqlDatabase.add_order(self.ID, self.email_client, self.amount, "entered")