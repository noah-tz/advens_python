class Ticket:
    def __init__(self, item_type, name, priority=0) -> None:
        self.item_type = item_type
        self.name = name
        self.priority = priority
        self.time_entered = 12
