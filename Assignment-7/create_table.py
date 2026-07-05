##Creating Table
from connect import creat_connection
connection= creat_connection()
cursor=connection.cursor()
query = """
CREATE TABLE IF NOT EXISTS contacts(
id SERIAL PRIMARY KEY,
name VARCHAR(100),
phone VARCHAR(20)
);
"""
cursor.execute(query)
connection.commit()
print("Table Created Succesfully")
cursor.close()
connection.close()
