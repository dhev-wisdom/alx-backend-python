#1/usr/bin/python3
import sqlite3

class ExecuteQuery:
    def __init__(self, db_name='users.db', query="SELECT * FROM users WHERE age > ?", parameter=25):
        self.db_name = db_name
        self.query = query
        self.parameter = parameter
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.parameter)
        return self.cursor.fetchall()
    
    def __exit__(self, type, value, traceback):
        if self.cursor():
            self.cursor.close()
        if self.conn:
            self.conn.close()
        if type:
            print(f"An error occured: {type}")
        return False

if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    age = (25,)

    with ExecuteQuery(query, age) as result:
        for row in result:
            print(row)