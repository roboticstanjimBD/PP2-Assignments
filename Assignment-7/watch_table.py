### Wathching data using SELECT
from connect import creat_connection
connection= creat_connection()
cursor=connection.cursor()
query = "SELECT * FROM contacts"
cursor.execute(query)
rows = cursor.fetchall()
print("_____ Contct List _____")
for row in rows:
    print(f"ID:{row[0]}")  ## Display all contacts
    print (f"Name:{row[1]}")      
    print(f"Phone:{row[2]}")
    print ("-" * 25)
    cursor.close()
    connection.close()