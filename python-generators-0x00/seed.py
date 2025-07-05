#!/usr/bin/python3
import mysql.connector
import csv
import uuid

def connect_db():
    try:
        connection = mysql.connector.connect(
            host= 'localhost',
            user= 'root',
            password= 'Wisdom20032000$',
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: ", {err})
        return None

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Wisdom20032000$',
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: ", {err})
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age DECIMAL NOT NULL
        )
    """)
    connection.commit()
    print("Table user_data has been created successfully")
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()
    with open(data, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("SELECT * FROM user_data WHERE email=%s", (row["email"],))
            if not cursor.fetchone():
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES(%s, %s, %s, %s)", (str(uuid.uuid4()), row['name'], row['email'], row['age'])
                )
    connection.commit()
    cursor.close()
