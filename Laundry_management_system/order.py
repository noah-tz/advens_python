from typing import Type
import settings



class Order:
    def __init__(self, email_client: str, NO: str) -> None:
        self.email_client = email_client 
        self.NO: str = NO
        self.items:dict = {}

    def calculate(self) -> int:
        sum_order: int = sum(settings.PRISE_LIST[item] * self.items[item] for item in self.items)
        return (max(settings.MIN_ORDER, sum_order))
    
    def add_item(self, item: str) -> bool:
        if item not in settings.PRISE_LIST:
            return False
        self.items[item] += 1
        return True