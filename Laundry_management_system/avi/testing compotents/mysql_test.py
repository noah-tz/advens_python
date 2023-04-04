import mysql.connector
import pandas as pd


my_database = mysql.connector.connect(
    host="localhost", user="avi", password="password", database="cleaners"
)


def read(conn):
    print("read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dinners")
    for row in cursor:
        print(f"row = {row}")
    print()


def read_as_pd(conn):
    query = "SELECT * FROM dinners"
    database = pd.read_sql(query, conn)
    print(database)
    print()


def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dinners(name,entree) values('dogs', 'cats')")
    conn.commit()
    read_as_pd(conn)


def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute("UPDATE dinners SET side = 'mayo' where name = 'dogs';")
    conn.commit()
    read_as_pd(conn)


def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dinners WHERE name = 'dogs'")
    conn.commit()
    read_as_pd(conn)


read(my_database)
create(my_database)
update(my_database)
delete(my_database)
