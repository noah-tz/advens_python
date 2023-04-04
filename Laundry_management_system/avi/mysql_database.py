import mysql.connector
from mysql.connector import Error, ProgrammingError
import pandas as pd


class MysqlDatabase:
    @staticmethod
    def checks_database(database_name: str) -> None:
        mysql_connection = mysql.connector.connect(
            host="localhost", user="noah", password="password"
        )
        main_cursor = mysql_connection.cursor()
        main_cursor.execute("SHOW DATABASES")
        databases_names = [name[0] for name in main_cursor]
        if database_name not in databases_names:
            with open("build_database.sql", "r") as fd:
                sql_instructions = fd.read()
            main_cursor.execute(sql_instructions)

    def __init__(self):
        self.__database_name = "laundry"
        self.checks_database(self.__database_name)
        self.__database = mysql.connector.connect(
            host="localhost",
            user="noah",
            password="password",
            database=self.__database_name,
        )

    def read(self, table_name: str, command: str = "*"):
        print("read")
        cursor = self.__database.cursor()
        cursor.execute(f"SELECT {command} FROM {table_name}")
        for row in cursor:
            print(f"row = {row}")
        print()

    def column_names(self, table_name: str):
        cursor = self.__database.cursor()
        cursor.execute(f"DESC {table_name}")
        return [row[0] for row in cursor]

    def print_by_pd(self, table_name: str):
        query = f"SELECT * FROM {table_name}"
        database = pd.read_sql(query, self.__database)
        print(database)
        print()

    def create(self, table_name: str, row_names: tuple, values: tuple) -> None:
        """insert information into database

        Args:
            table_name (str): table name to insert the data
            row_names (tuple): names of the rows to enter the values ex: ('name','value')
            values (tuple): values to insert in the database ex: ('charlie','straw')
        """
        print("Create")
        cursor = self.__database.cursor()
        cursor.execute(f"INSERT INTO {table_name}{row_names} VALUES{values}")
        self.__database.commit()
        self.print_by_pd(table_name)

    def update(self, table_name: str, to_update, line_condition):
        print("Update")
        cursor = self.__database.cursor()
        cursor.execute(f"UPDATE {table_name} SET {to_update} WHERE {line_condition};")
        self.__database.commit()
        self.print_by_pd(table_name)

    def delete(self, table_name: str, line_condition: str, value: str) -> None:
        """deletes lines in the database

        function that deletes lines in the database by line condition

        Args:
            line_condition (str): condition to delete
            value (str): that needs to be deleted
        """
        print("Delete")
        cursor = self.__database.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE {line_condition} = '{value}'")
        self.__database.commit()
        self.print_by_pd(table_name)

MysqlDatabase.checks_database("laundry")