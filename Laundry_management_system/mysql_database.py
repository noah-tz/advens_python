import mysql.connector
import pandas as pd
import settings


class SqlOrders:
    @staticmethod
    def add_order(order_id: str, client_email: str, order_amount: float, stage: str = "entered", order_notes: str = None) -> None:
        """Adds an order to the 'orders' table in the database.

        Args:
            order_id (str): The ID of the order to add.
            client_email (str): The email address of the client who made the order.
            order_amount (float): The amount of the order.
            stage (str, optional): The stage of the order. Defaults to "entered".
            order_notes (str, optional): Notes on the order. Defaults to None.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        query = "INSERT INTO orders (order_id, client_email, order_amount, stage, order_notes) VALUES (%s, %s, %s, %s, %s)"
        values = (order_id, client_email, order_amount, stage, order_notes)
        cursor.execute(query, values)
        MysqlDatabase._mysql_connection.commit()
        MysqlDatabase.print_by_pd("orders")

    @staticmethod
    def check_order_existence(order_id: str) -> bool:
        """Checks whether an order with the given ID exists in the 'orders' table in the database.

        Args:
            order_id (str): The ID of the order to check.

        Returns:
            bool: True if an order with the given ID exists in the 'orders' table, False otherwise.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        cursor.execute(
            "SELECT order_id FROM orders WHERE order_id = %s", (order_id,))
        return bool(cursor.fetchone())


    @staticmethod
    def check_start_ID_orders():
        """Checks the start ID for orders.

        Returns:
            int: The start ID for orders.
        """
        MysqlDatabase.checks_database()
        cursor = MysqlDatabase._mysql_connection.cursor()
        cursor.execute("SELECT MAX(order_id) FROM orders")
        result = cursor.fetchone()
        return settings.START_ORDERS_ID if result[0] is None else int(result[0] + 1)


class SqlClients:
    @staticmethod
    def add_client(name: str, family_name: str, city: str, street: str, house_number: int, phone: str, client_email: str, client_password: str, message_type: str = "email") -> None:
        """
        Adds a client to the 'clients' table in the database.

        Args:
            name (str): The name of the client.
            family_name (str): The family name of the client.
            city (str): The city in which the client resides.
            street (str): The street on which the client resides.
            house_number (int): The house number of the client.
            phone (str): The phone number of the client.
            client_email (str): The email address of the client.
            message_type (str, optional): The message type used to communicate with the client. Defaults to "email".
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        query = "INSERT INTO clients (name, family_name, city, street, house_number, phone, client_email, client_password, message_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, family_name, city, street, house_number, phone, client_email, client_password, message_type)
        cursor.execute(query, values)
        MysqlDatabase._mysql_connection.commit()
        MysqlDatabase.print_by_pd("clients")


    @staticmethod
    def check_client_existence(email_client: str) -> bool:
        """
        Checks whether a client with the given email address exists in the 'clients' table in the database.

        Args:
            email_client (str): The email address of the client to check.

        Returns:
            bool: True if a client with the given email address exists in the 'clients' table, False otherwise.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        query = "SELECT client_email FROM clients WHERE client_email = %s"
        cursor.execute(query, (email_client,))
        return bool(cursor.fetchone())
    
    @staticmethod
    def get_client_password(email_client: str) -> str:
        """
        Returns the password of a client with the given email address from the 'clients' table in the database.

        Args:
            email_client (str): The email address of the client to get the password for.

        Returns:
            str: The password of the client with the given email address, or an empty string if no such client exists.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        query = "SELECT client_password FROM clients WHERE client_email = %s"
        cursor.execute(query, (email_client,))
        result = cursor.fetchone()
        return result[0] if result is not None else ""





class SqlVariables:
    @staticmethod
    def insert_variable(variable_name: str, variable_value: str) -> None:
        """
        Inserts a new variable name and value into the database.

        :param variable_name: The name of the variable to insert.
        :param variable_value: The value of the variable to insert.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        insert_query = "INSERT INTO variables (variable_name, variable_value) VALUES (%s, %s)"
        values = (variable_name, variable_value)
        cursor.execute(insert_query, values)
        MysqlDatabase._mysql_connection.commit()

    @staticmethod
    def delete_variable(variable_name: str) -> None:
        """
        Deletes a variable and its corresponding value from the database.

        :param variable_name: The name of the variable to delete.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        delete_query = "DELETE FROM variables WHERE variable_name = %s"
        values = (variable_name,)
        cursor.execute(delete_query, values)
        MysqlDatabase._mysql_connection.commit()

    @staticmethod
    def get_variable(variable_name: str) -> str:
        """
        Retrieves the value of a variable from the database.

        :param variable_name: The name of the variable to retrieve.
        :return: The value of the variable, or None if it does not exist.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        select_query = "SELECT variable_value FROM variables WHERE variable_name = %s"
        values = (variable_name,)
        cursor.execute(select_query, values)
        return result[0] if (result := cursor.fetchone()) else None

    @staticmethod
    def update_variable(variable_name: str, new_value: str) -> None:
        """
        Updates the value of a variable in the database.

        :param variable_name: The name of the variable to update.
        :param new_value: The new value for the variable.
        """
        MysqlDatabase.checks_database()
        cursor = MysqlDatabase._mysql_connection.cursor()
        update_query = "UPDATE variables SET variable_value = %s WHERE variable_name = %s"
        values = (new_value, variable_name)
        cursor.execute(update_query, values)
        MysqlDatabase._mysql_connection.commit()


    
class SqlEquipment:
    @staticmethod
    def add_type_equipment(equipment_name: str, equipment_value: int = 0) -> None:
        """
        Adds a new type of equipment to the 'equipment' table with the given name and value.
        
        Args:
        - equipment_name: str, the name of the new equipment type.
        - equipment_value: int (default=0), the value of the new equipment type.
        
        Returns: None
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        insert_query = "INSERT INTO equipment (equipment_name, equipment_value) VALUES (%s, %s)"
        values = (equipment_name, equipment_value)
        cursor.execute(insert_query, values)
        MysqlDatabase._mysql_connection.commit()

    @staticmethod
    def delete_type_equipment(equipment_name: str) -> None:
        """
        Deletes a type of equipment from the 'equipment' table with the given name.
        
        Args:
        - equipment_name: str, the name of the equipment type to delete.
        
        Returns: None
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        delete_query = "DELETE FROM equipment WHERE equipment_name = %s"
        values = (equipment_name,)
        cursor.execute(delete_query, values)
        MysqlDatabase._mysql_connection.commit()

    @staticmethod
    def get_equipment_value(equipment_name: str) -> int or None:
        """
        Retrieves the value of the equipment type with the given name from the 'equipment' table.
        
        Args:
        - equipment_name: str, the name of the equipment type to retrieve the value for.
        
        Returns:
        - int or None: the value of the equipment type if it exists, or None if it does not.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        select_query = "SELECT equipment_value FROM equipment WHERE equipment_name = %s"
        values = (equipment_name,)
        cursor.execute(select_query, values)
        return result[0] if (result := cursor.fetchone()) else None

    @staticmethod
    def update_equipment_value(equipment_name: str, new_value: int) -> None:
        """
        Updates the value of the equipment type with the given name in the 'equipment' table to the new value.
        
        Args:
        - equipment_name: str, the name of the equipment type to update.
        - new_value: int, the new value for the equipment type.
        
        Returns: None
        """
        MysqlDatabase.checks_database()
        cursor = MysqlDatabase._mysql_connection.cursor()
        update_query = "UPDATE equipment SET equipment_value = %s WHERE equipment_name = %s"
        values = (new_value, equipment_name)
        cursor.execute(update_query, values)
        MysqlDatabase._mysql_connection.commit()






class MysqlDatabase(SqlOrders, SqlClients, SqlVariables, SqlEquipment):
    """
    This class provides methods to interact with a MySQL database using the mysql-connector-python package.
    """

    # Initialize a MySQL connection object
    _mysql_connection = mysql.connector.connect(
        host=settings.HOST_SQL, user=settings.USER_SQL, password=settings.PASSWORD_SQL)

    @staticmethod
    def checks_database() -> None:
        """
        Check if the database exists, and create it if it does not exist.

        Args:
            None

        Returns:
            None
        """
        main_cursor = MysqlDatabase._mysql_connection.cursor()
        main_cursor.execute("SHOW DATABASES")
        databases_names = [name[0] for name in main_cursor]
        if settings.NAME_DATABASE_SQL not in databases_names:
            with open("/home/noah-tz/Documents/works/advens_python/Laundry_management_system/build_database.sql", "r") as fd:
                sql_instructions = fd.read()
            main_cursor.execute(sql_instructions)
        MysqlDatabase._mysql_connection = mysql.connector.connect(
            host=settings.HOST_SQL, user=settings.USER_SQL, password=settings.PASSWORD_SQL, database=settings.NAME_DATABASE_SQL)

    @staticmethod
    def read(table_name: str, command: str = "*") -> None:
        """
        Select data from the specified table in the MySQL database and print the results.

        Args:
            table_name (str): The name of the table to select data from.
            command (str): Optional SQL command to execute, defaults to "*".

        Returns:
            None
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        cursor.execute(f"SELECT {command} FROM {table_name}")
        for row in cursor:
            print(f"row = {row}")
        print()

    @staticmethod
    def column_names(table_name: str) -> list:
        """
        Retrieve the column names of a specified table in the MySQL database.

        Args:
            table_name (str): The name of the table to retrieve column names from.

        Returns:
            List[str]: A list of column names.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        cursor.execute(f"DESC {table_name}")
        return [row[0] for row in cursor]

    @staticmethod
    def print_by_pd(table_name: str) -> None:
        """
        Select all data from the specified table in the MySQL database using pandas and print the results.

        Args:
            table_name (str): The name of the table to select data from.

        Returns:
            None
        """
        query = f"SELECT * FROM {table_name}"
        database = pd.read_sql(query, MysqlDatabase._mysql_connection)
        print(database)
        print()

    @staticmethod
    def create(table_name: str, row_names: tuple[str], values: tuple[str]) -> None:
        """
        Insert a new row of data into the specified table in the MySQL database.

        Args:
            table_name (str): The name of the table to insert data into.
            row_names (Tuple[str]): A tuple of strings representing the column names to insert data into.
            values (Tuple[str]): A tuple of strings representing the values to insert into the specified columns.

        Returns:
            None
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        cursor.execute(f"INSERT INTO {table_name} {row_names} VALUES {values}")
        MysqlDatabase._mysql_connection.commit()
        MysqlDatabase.print_by_pd(table_name)

    @staticmethod
    def update(table_name: str, to_update: str, line_condition: str) -> None:
        """
        Updates rows in a MySQL table based on a condition.

        Args:
        - table_name (str): The name of the MySQL table to update.
        - to_update (str): A string representing the column(s) to update and their new values. 
                           The format is "column1=new_value1, column2=new_value2, ...".
        - line_condition (str): A string representing the condition that must be met for a row to be updated.
                                The format is "column_name='value'".

        Returns:
        - None.
        """
        print("Update")
        cursor = MysqlDatabase._mysql_connection.cursor()
        cursor.execute(
            f"UPDATE {table_name} SET {to_update} WHERE {line_condition};")
        MysqlDatabase._mysql_connection.commit()
        MysqlDatabase.print_by_pd(table_name)

    @staticmethod
    def get_value_from_table(table_name: str, column_name: str, row_id: int, column_id: str):
        """
        Fetches the value of a specific column in a specific row of a MySQL table.

        Args:
            table_name (str): The name of the table to query.
            column_name (str): The name of the column to fetch the value from.
            row_id (int): The unique identifier of the row to fetch the value from.
            column_id (str): The name of the column that contains the row identifier.

        Returns:
            The value of the specified column in the specified row, or None if the row is not found.
        """
        cursor = MysqlDatabase._mysql_connection.cursor()
        cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE {column_id} = %s", (row_id,))
        result = cursor.fetchone()
        return result[0] if result else None

        

    @staticmethod
    def delete(table_name: str, line_condition: str, value: str) -> None:
        """
        Deletes rows from a MySQL table based on a condition.

        Args:
        - table_name (str): The name of the MySQL table to delete from.
        - line_condition (str): A string representing the condition that must be met for a row to be deleted.
                                The format is "column_name='value'".
        - value (str): The value that must match the condition in line_condition in order for a row to be deleted.

        Returns:
        - None.
        """
        print("Delete")
        cursor = MysqlDatabase._mysql_connection.cursor()
        cursor.execute(
            f"DELETE FROM {table_name} WHERE {line_condition} = '{value}'")
        MysqlDatabase._mysql_connection.commit()
        MysqlDatabase.print_by_pd(table_name)

    @staticmethod
    def drop_table(table_name: str) -> None:
        """
        Drops a MySQL table if it exists.

        Args:
        - table_name (str): The name of the MySQL table to drop.

        Returns:
        - None.
        """
        with MysqlDatabase._mysql_connection.cursor() as cursor:
            drop_query = f"DROP TABLE IF EXISTS {table_name}"
            cursor.execute(drop_query)
            MysqlDatabase._mysql_connection.commit()

    @staticmethod
    def drop_database() -> None:
        """
        Drops the database with the name specified in the `settings.NAME_DATABASE_SQL` variable,
        if it exists. This method should be used with caution, as it will permanently delete
        all data in the database.

        Args:
            None

        Returns:
            None
        """
        with MysqlDatabase._mysql_connection.cursor() as cursor:
            drop_query = f"DROP DATABASE IF EXISTS {settings.NAME_DATABASE_SQL}"
            cursor.execute(drop_query)
            MysqlDatabase._mysql_connection.commit()



# MysqlDatabase.drop_database()
# MysqlDatabase.check_start_ID_orders()
# MysqlDatabase.add_client("noah", "tzitrenboim", "miryamssssss",
#                          "miryam", 4444, "0500000000", "t0527184022@gmail.com", "123456", "email")
# MysqlDatabase.add_order(MysqlDatabase.check_start_ID_orders(),
#                         "t0527184022@gmail.com", 128, "entered")
# MysqlDatabase.add_order(
#     MysqlDatabase.check_start_ID_orders(), "teyyycycyyd", 111)
# print(MysqlDatabase.column_names("clients"))
# print(MysqlDatabase.column_names("orders"))
# print(MysqlDatabase.column_names("variables"))



