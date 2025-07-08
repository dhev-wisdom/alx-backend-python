import time
import sqlite3 
import functools

#### paste your with_db_decorator here
def with_db_connection(func):
    """ your code goes here""" 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users_db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

""" your code goes here"""
def retry_on_failure(retries, delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            number_of_tries = 0
            while number_of_tries < retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    number_of_tries += 1
                    if number_of_tries < retries:
                        print(f"An error was encountered: {e} \nTry again")
                        time.sleep(delay)
                    else:
                        print("You have tried the maximum number of times. Raising error")
                        raise
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)