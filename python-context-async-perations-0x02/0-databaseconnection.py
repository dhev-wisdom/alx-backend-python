#1/usr/bin/python3
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def __exit__(self, type, value, traceback):
        if self.conn:
            self.conn.close()
        if type:
            print(f"An error occured: {type}")
        return False

    
if __name__ == "__main__":
    with DatabaseConnection as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)