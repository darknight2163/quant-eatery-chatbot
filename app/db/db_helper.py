import os, sqlite3
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)

def get_connection():
    return sqlite3.connect(DB_PATH)

def insert_order_item(item_name, quantity, order_id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            # Get price of the item
            cursor.execute(
                "SELECT item_id, price FROM food_items WHERE name = ?",
                (item_name,)
            )
            result = cursor.fetchone()
            if result is None:
                return -1
            item_id = result[0]
            price = result[1]
            total_price = price * quantity
            cursor.execute("""
                INSERT INTO orders (order_id, item_id, quantity, total_price)
                VALUES (?, ?, ?, ?)
            """, (order_id, item_id, quantity, total_price))
            conn.commit()
        return 1

    except Exception as e:
        print(f"Error inserting order item: {e}")
        return -1


def insert_order_tracking(order_id, status):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO order_tracking (order_id, status)
            VALUES (?, ?)
        """, (order_id, status))
        conn.commit()


def get_total_order_price(order_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT SUM(total_price)
            FROM orders
            WHERE order_id = ?
        """, (order_id,))
        result = cursor.fetchone()[0]
    return result if result else 0

def get_next_order_id():
    from datetime import datetime
    # Use seconds-level precision, fits safely in a 64-bit int
    order_id = int(datetime.now().strftime('%y%m%d%H%M%S'))
    return order_id

def get_order_status(order_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT status
            FROM order_tracking
            WHERE order_id = ?
        """, (order_id,))
        result = cursor.fetchone()
    return result[0] if result else None


if __name__ == "__main__":
    print(get_next_order_id())