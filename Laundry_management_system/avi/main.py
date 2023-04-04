from mysql_database import MysqlDatabase

instance_class = MysqlDatabase()
print(instance_class.column_names("orders"))
# instance_class.print_by_pd()
instance_class.create(
    "orders", "(order_id, client_id, stage)", ("dogs", "cats", "washed")
)
# instance_class.delete("name", "dogs")
