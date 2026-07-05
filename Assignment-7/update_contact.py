
###Update Contact:

from connect import creat_connection
connection= creat_connection()
cursor=connection.cursor()
name = input("Enter the contact name to search:")
new_phone= input("Enter the new phone number:")

query = """
UPDATE contacts
SET phone = %s
WHERE name = %s
"""
cursor.execute(query, (new_phone, name))
connection.commit()

# Check whether any row was updated
if cursor.rowcount > 0:
    print("Contact updated successfully!")
else:
    print("Contact not found!")

cursor.close()
connection.close()