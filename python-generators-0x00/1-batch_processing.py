#!/usr/bin/python3

seed = __import__("seed")

def stream_users_in_batches(batch_size):
    """function fetches rows in batches of `batch_size`"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    total_rows = 0
    offset = 0
    batch_num = 1
    
    while True:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch
        offset += batch_size
        total_rows += 1
        batch_num += 1

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """function processes each batch to filter users over the age of 25"""
    for batch in stream_users_in_batches(batch_size):
        filteredUsers = [user for user in batch if user[3] > 25]
        yield filteredUsers

if __name__ == "__main__":
    batch_processing_ = batch_processing(50)