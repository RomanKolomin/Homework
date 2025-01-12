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


def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    all_product = cursor.fetchall()

    connection.close()
    return all_product


if __name__ == "__main__":
    create_database()
