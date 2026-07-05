
### Search Contact:

from connect import creat_connection
connection= creat_connection()
cursor=connection.cursor()
name = input("Enter the contact name to search:")

query="""
SELECT * FROM contacts 
WHERE name = %s
"""

cursor.execute(query,(name,))
rows= cursor.fetchall()


# Check whether any record was found
if rows:
    print("\nContact Found:\n")

    for row in rows:
        print(f"ID    : {row[0]}")
        print(f"Name  : {row[1]}")
        print(f"Phone : {row[2]}")
        print("-" * 25)
else:
    print("No contact found.")

# Close cursor
cursor.close()

# Close connection
connection.close()
