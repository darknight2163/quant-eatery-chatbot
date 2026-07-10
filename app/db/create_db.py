import os
import sqlite3
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_PATH = Path(__file__).parent / DB_NAME

def create_database(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS food_items (
        item_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER,
        item_id INTEGER,
        quantity INTEGER,
        total_price REAL,
        PRIMARY KEY (order_id, item_id),
        FOREIGN KEY (item_id) REFERENCES food_items(item_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_tracking (
        order_id INTEGER PRIMARY KEY,
        status TEXT
    )
    """)

    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM food_items")
    if cursor.fetchone()[0] == 0:

        food_items = [
            (1, "Butter Chicken", 250.00),
            (2, "Chicken Biryani", 230.00),
            (3, "Paneer Butter Masala", 180.00),
            (4, "Masala Dose", 90.00),
            (5, "Chole Bhature", 100.00),
            (6, "Dal Makhani", 140.00),
            (7, "Palak Paneer", 150.00),
            (8, "Veg Pulao", 180.00),
            (9, "Garlic Naan", 110.00),
        ]

        cursor.executemany(
            "INSERT INTO food_items VALUES (?, ?, ?)",
            food_items
        )

        orders = [
            (40, 1, 2, 500.00),
            (40, 3, 1, 180.00),
            (41, 4, 3, 270.00),
            (41, 6, 2, 280.00),
            (41, 9, 4, 440.00),
        ]

        cursor.executemany(
            "INSERT INTO orders VALUES (?, ?, ?, ?)",
            orders
        )

        tracking = [
            (40, "delivered"),
            (41, "in transit"),
        ]

        cursor.executemany(
            "INSERT INTO order_tracking VALUES (?, ?)",
            tracking
        )

    conn.commit()
    conn.close()

def initialize_database():
    if not os.path.exists(DB_PATH):
        print("Database not found. Creating database...")
        create_database(DB_PATH)
        print("Database created successfully!")
    else:
        print("Database already exists. Skipping creation.")