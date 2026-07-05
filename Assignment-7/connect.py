import psycopg2
from config import host, database, user, password, port

def create_connection():
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    return connection


if __name__ == "__main__":
    connection = creat_connection()
    print("Connection Successful!")