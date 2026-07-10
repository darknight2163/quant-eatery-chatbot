import os
import sqlite3
import pandas as pd

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "app", "db", "quant_eatery.db")
conn = sqlite3.connect(DB_PATH)

# Get all table names
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)

for table in tables["name"]:
    print(f"\n{'='*50}")
    print(f"TABLE: {table}")
    print('='*50)
    df = pd.read_sql(f"SELECT * FROM {table} LIMIT 10;", conn)
    print(df)

conn.close()