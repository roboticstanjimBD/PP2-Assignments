
# Add a new contact manually
def add_contact():

    connection = create_connection()
    cursor = connection.cursor()

    # Take input from the user
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    # SQL query
    query = """
    INSERT INTO contacts(name, phone)
    VALUES (%s, %s)
    """

    # Execute the query
    cursor.execute(query, (name, phone))

    # Save changes
    connection.commit()

    print("Contact added successfully!")

    cursor.close()
    connection.close()



#### Making Perfect for Console:
import csv
from connect import create_connection


# Import contacts from CSV file
def import_csv():

    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO contacts(name, phone)
    VALUES (%s, %s)
    """

    with open("contact.csv", "r") as file:

        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Insert each row into the database
        for row in reader:
            cursor.execute(query, (row[0], row[1]))

    connection.commit()

    print("CSV imported successfully!")

    cursor.close()
    connection.close()


# Display all contacts
def show_contacts():

    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM contacts"

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\n------ Contact List ------")

    for row in rows:
        print(f"ID    : {row[0]}")
        print(f"Name  : {row[1]}")
        print(f"Phone : {row[2]}")
        print("-" * 25)

    cursor.close()
    connection.close()


# Search contact by name
def search_contact():

    connection = create_connection()
    cursor = connection.cursor()

    name = input("Enter contact name: ")

    query = """
    SELECT * FROM contacts
    WHERE name = %s
    """

    cursor.execute(query, (name,))

    rows = cursor.fetchall()

    if rows:

        print("\nContact Found\n")

        for row in rows:
            print(f"ID    : {row[0]}")
            print(f"Name  : {row[1]}")
            print(f"Phone : {row[2]}")
            print("-" * 25)

    else:
        print("Contact not found!")

    cursor.close()
    connection.close()


# Update phone number
def update_contact():

    connection = create_connection()
    cursor = connection.cursor()

    name = input("Enter contact name: ")
    new_phone = input("Enter new phone number: ")

    query = """
    UPDATE contacts
    SET phone = %s
    WHERE name = %s
    """

    cursor.execute(query, (new_phone, name))

    connection.commit()

    if cursor.rowcount > 0:
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

    cursor.close()
    connection.close()


# Delete contact
def delete_contact():

    connection = create_connection()
    cursor = connection.cursor()

    name = input("Enter contact name: ")

    query = """
    DELETE FROM contacts
    WHERE name = %s
    """

    cursor.execute(query, (name,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

    cursor.close()
    connection.close()


# Main menu
while True:

    print("\n---- PhoneBook Menu ----")
    print("1. Add Contact (Console)")
    print("2. Import from CSV")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        import_csv()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        search_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")