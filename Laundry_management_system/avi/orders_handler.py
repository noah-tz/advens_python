class OrderHandler:
    def __init__(self):
        self.__table_name = "orders"
        self.__values = (
            "( order_id, client_id, order_type, order_amount, stage_finished_at, stage)"
        )
        self.__order_number = 0

    def new_order(self, sql_database: object, inputs: list[str]) -> str:
        inputs_to_add = []
        sql_database.create(self.__table_name, self.__values, inputs_to_add)
