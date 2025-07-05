# Python-MySQL Seeder Script

This project sets up a MySQL database (`ALX_prodev`), creates a table (`user_data`), and populates it using a CSV file — all through a Python script. It also demonstrates how to stream data from the database using generators for efficient processing.

## 📁 Project Structure

.
├── seed.py # Python script to set up and seed the database
├── user_data.csv # Sample user data
├── 0-main.py # Entry point to run the seeding process


## ⚙️ What It Does

- Connects to MySQL server.
- Creates a new database `ALX_prodev` (if it doesn't exist).
- Creates the `user_data` table with the following fields:
  - `user_id` (UUID, Primary Key)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Reads data from `user_data.csv` and inserts it into the table.
- Demonstrates usage of Python generators for efficient row handling.

## 🚀 How to Run

1. **Ensure MySQL is installed** and running on your machine.
2. **Add MySQL to your system PATH** so you can run it via `mysql -u root -p`.
3. **Install dependencies** (if any):
   ```bash
   pip install mysql-connector-python
