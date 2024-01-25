import sqlite3

class UserDatabase:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_table(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     email TEXT,
                     age INTEGER,
                     address TEXT)''')
        conn.commit()
        conn.close()

    def insert_user(self, name, email, age, address):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email, age, address) VALUES (?, ?, ?, ?)",
                  (name, email, age, address))
        conn.commit()
        conn.close()

    def get_all_users(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        rows = c.fetchall()
        conn.close()
        return rows
def main():
    db = UserDatabase('users.db')
    db.create_table()

    # Insert 5 users
    db.insert_user('John Doe', 'john@example.com', 25, '123 Main St')
    db.insert_user('Jane Smith', 'jane@example.com', 30, '456 Elm St')
    db.insert_user('Mike Johnson', 'mike@example.com', 35, '789 Oak St')
    db.insert_user('Sarah Williams', 'sarah@example.com', 28, '321 Pine St')
    db.insert_user('David Brown', 'david@example.com', 32, '654 Maple St')

    # Select a user based on a WHERE clause
    user = db.get_all_users()
    selected_user = [row for row in user if row[1] == 'John Doe']
    print(selected_user)

if __name__ == '__main__':
    main()
