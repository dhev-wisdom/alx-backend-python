import sqlite3
import functools
# import logging
from datetime import datetime

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#### decorator to lof SQL queries
def log_queries(func):
    """ YOUR CODE GOES HERE"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        print(f"[{datetime.now()}]: {query}")
        # logging.info(query)
        return func(*args, **kwargs)
    return wrapper
        

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")