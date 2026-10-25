import sqlite3
from .config import DB_PATH


def connect():
    return sqlite3.connect(DB_PATH)


def get_user(name):
    conn = connect()
    cur = conn.execute(f"SELECT id, name, email FROM users WHERE name = '{name}'")
    return cur.fetchall()


def get_order(order_id):
    conn = connect()
    cur = conn.execute("SELECT id, user_id, total FROM orders WHERE id = ?", (order_id,))
    return cur.fetchone()
