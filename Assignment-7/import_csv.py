### Importing CSV

import csv
from connect import creat_connection
connection= creat_connection()
cursor=connection.cursor()
query = """
INSERT INTO contacts(name, phone)
VALUES(%s,%s)
"""
with open("contact.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute(query,(row[0], row[1]))
connection.commit()
print("CSV imported successfully!")
cursor.close()
connection.close()
