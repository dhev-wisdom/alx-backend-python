#!/usr/bin/python3

seed = __import__('seed')

def stream_users():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
    connection.close

if __name__ == "__main__":
    stream_users = stream_users