import sqlite3


def create_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f'Продукт {i}', f' Описание {i}', f'{i}00'))

    connection.commit()
    connection.close()


def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    all_product = cursor.execute("SELECT * FROM Products").fetchall()

    connection.close()
    return all_product


def check_user():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    users_registred = cursor.execute("SELECT username FROM Users")
    message = ""
    for user in users_registred:
        message += f' {user[0]} \n'

    connection.close()
    return message


def add_user(username, email, age):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    is_included = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))

    if is_included:
        cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    initiate_db()
