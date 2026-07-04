import psycopg2
import csv
from config import load_config

# Database connection
def get_db_connection():
    config = load_config()
    return psycopg2.connect(**config)

# 1. Design table
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# 2. Insert from CSV
def insert_from_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            conn = get_db_connection()
            cur = conn.cursor()
            for row in reader:
                cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()
            cur.close()
            conn.close()
            print("CSV data imported successfully!")
    except Exception as e:
        print(f"Error importing CSV: {e}")

# 3. Add contact from console
def add_contact(name, phone):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Contact added successfully!")

# 4. Update contact
def update_contact(name, new_phone):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    count = cur.rowcount
    cur.close()
    conn.close()
    print(f"{count} contact(s) updated.")

# 5. Query with filters
def search_contacts(filter_type, value):
    conn = get_db_connection()
    cur = conn.cursor()
    if filter_type == '1': # Search by name
        cur.execute("SELECT * FROM contacts WHERE name LIKE %s", ('%' + value + '%',))
    else: # Search by phone prefix
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (value + '%',))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    cur.close()
    conn.close()

# 6. Delete contact
def delete_contact(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
    conn.commit()
    count = cur.rowcount
    cur.close()
    conn.close()
    print(f"{count} contact(s) deleted.")

# Main Menu
if __name__ == "__main__":
    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Add Contact (Console)\n2. Import from CSV\n3. Update Contact\n4. Search Contact\n5. Delete Contact\n6. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            add_contact(input("Name: "), input("Phone: "))
        elif choice == '2':
            insert_from_csv(input("Enter CSV filename: "))
        elif choice == '3':
            update_contact(input("Name: "), input("New Phone: "))
        elif choice == '4':
            print("1. Search by Name\n2. Search by Phone Prefix")
            f_type = input("Choice: ")
            search_contacts(f_type, input("Enter value: "))
        elif choice == '5':
            delete_contact(input("Name to delete: "))
        elif choice == '6':
            break