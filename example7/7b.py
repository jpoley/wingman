import sqlite3

class UserDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                email TEXT
            )
        ''')
        self.conn.commit()

    def insert_user(self, name, age, email):
        self.cursor.execute('''
            INSERT INTO users (name, age, email)
            VALUES (?, ?, ?)
        ''', (name, age, email))
        self.conn.commit()

    def select_user(self, where_clause):
        self.cursor.execute('''
            SELECT * FROM users
            WHERE {}
        '''.format(where_clause))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

def main():
    db = UserDatabase('/path/to/database.db')

    # Insert 5 users
    db.insert_user('John Doe', 25, 'john@example.com')
    db.insert_user('Jane Smith', 30, 'jane@example.com')
    db.insert_user('Bob Johnson', 35, 'bob@example.com')
    db.insert_user('Alice Brown', 28, 'alice@example.com')
    db.insert_user('Mike Davis', 32, 'mike@example.com')

    # Select a user based on a WHERE clause
    user = db.select_user('name = "John Doe"')
    print(user)

    db.close()

if __name__ == '__main__':
    main()
