
### Delete from the contact:


from connect import creat_connection
connection= creat_connection()
cursor=connection.cursor()
name = input("Enter the contact name to delete:")

query= """
DELETE FROM contacts
WHERE name = %s
"""
cursor.execute(query,(name,))
if cursor.rowcount > 0:
    print("Contact Deleted Successfully!")
else:
    print("Contact not found!")
    cursor.close()
    connection.close()
