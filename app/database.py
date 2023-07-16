import sqlite3 as sq

db = sq.connect("tg.db")
cur = db.cursor()


async def db_start():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS accounts"
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "cart_id TEXT)"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS tickets"
        "(t_id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "direction TEXT, "
        "fly_date TEXT, "
        "price TEXT)"
    )
    db.commit()
