# 🗃️ SQL Query Logger with Python Decorator

## 📌 Overview

This project demonstrates how to use Python decorators to log SQL queries before they are executed. It's a practical and professional way to add logging functionality without modifying the original query function.

---

## 🧠 Concepts Covered

- Python decorators (`@log_queries`)
- `functools.wraps` to preserve function metadata
- SQLite database connection and querying
- Logging SQL queries dynamically from function arguments

---

## 🔧 File Descriptions

- `main.py` – Entry point that runs the function to fetch users.
- `0-log_queries.py` – Contains the `log_queries` decorator.
- `users.db` – SQLite database (should contain a `users` table).
- `README.md` – This file.

---

## 🧪 Sample Usage

```python
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Run
users = fetch_all_users(query="SELECT * FROM users")
